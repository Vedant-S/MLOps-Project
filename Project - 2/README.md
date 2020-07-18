# MLOps Project-2:
____________________________________________________________________________________________________________________
### DevOps Automation using Jenkins:
`Integrating Docker and Jenkins to perform Testing & Monitoring`
____________________________________________________________________________________________________________________
### PROBLEM STATEMENT:
- JOB 1: Pull the Github repository automatically when some developers push the repository to Github.
- JOB 2: By looking at the code or program file, Jenkins should automatically start the respective language interpreter and install image container to deploy code.
- JOB 3: Test your app if it is working or not.
- JOB 4: If the app is not working, then send an email to the developer with error messages.
____________________________________________________________________________________________________________________
### Pre-Requisites:
We are assuming that Docker, Git, and Jenkins with the Git Plugin are installed in the system.
____________________________________________________________________________________________________________________
### Description:
____________________________________________________________________________________________________________________
1. Setting up the Docker Container:
____________________________________________________________________________________________________________________
For setting up this container, we are going to use the centos image from DockerHub.
To download the image to our local machine, we have to run the following command from the Command Line:
docker pull centos
After installing the image, we need to modify the image so that we can run our PHP files in the container. We will be using Dockerfile to build our custom image.
To create the custom image, we need to create an empty file named Dockerfile anywhere in our host machine.

The contents of the Dockerfile will be as follows:

```
FROM centos

RUN yum install epel-release -y &&\
    yum update -y &&\
    yum install wget -y &&\
    yum install net-tools -y &&\
    yum install python36 -y &&\
    yum install httpd -y &&\
    yum install sudo -y &&\
    yum install git -y &&\    
    yum update -y
```
After making the Dockerfile we need to build it to create our image using:
`docker build -t apache:v1.`(from the same folder)
This would create our Apache image in the local machine.
____________________________________________________________________________________________________________________
2. Building the Jenkins Pipeline:
____________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________
2.1. Job-1: Automatic Code Download:
____________________________________________________________________________________________________________________
- Before downloading the code, we need to create some folders on our local machine which would act as volumes for the Docker containers.
- To create the folders in our local machine:
```
mkdir /root/Desktop/files
cd /root/Desktop/files/
mkdir php others
```

- First, the downloaded codes would be copied in the files directory.
- For creating the Job for downloading codes:
1. Select new item option from the Jenkins menu.
2. Assign a name to the Job ( eg. files_download )and select it to be a Freestyle project.
3. From the Configure Job option, we set the configurations.
4. From the Source Code Management section, we select Git and mention the URL of our GitHub Repository and select the branch as master.
5. In the Build Triggers section, we select Poll SCM and set the value to * * * * *. This means that the Job would check any code change from GitHub every minute.
6. In the Build Section, we type the following script: sudo cp -v -r -f * /root/Desktop/filesThis command would copy all the content downloaded from the GitHub master branch to the specified folder for deployment.
7. On clicking the Save option, we add the Job to our Job List.

- On coming back to the Job List page, we can see the Job is being built. If the colour of the ball turns blue, it means the Job has been successfully executed. If the colour changes to red, it means there has been some error in between. We can see the console output to check the error.
`Till now, we have successfully downloaded the codes from GitHub to our Server System automatically.`
____________________________________________________________________________________________________________________
2.2. Job-2: Classifying the files based on the Language of file:
____________________________________________________________________________________________________________________
Once the files have been downloaded, we need to copy the files to their respective folders automatically.
For creating the Job for classifying the files:
1. Select new item option from the Jenkins menu.
2. Assign a name to the Job ( eg. files_classification )and select it to be a Freestyle project.
3. From the Configure Job option, we set the configurations.
4. From the Build Triggers section, we select Build after other projects are built and mention files_download as the project to watch. This is called a DownStreaming Job.
5. In the Build Section, we type the following script:
```
sudo cp -rvf /root/Desktop/files/ *

if sudo grep -r php *
then
file=$(sudo grep -r Conv2D * | cut -d ":" -f 1)
sudo cp -rf $file /root/Desktop/files/php
sudo docker container run -dit -p 85:80 -v /root/Desktop/files/php:/usr/local/apache2/htdocs/  --name php_container apache:v1
```
6. On clicking the Save option, we add the Job to our Job List.

`Thus, we have successfully transferred the files to their respective folders. Also, we have set these folders as volumes of the Docker Containers and started the service.`
____________________________________________________________________________________________________________________
2.3. Job-3: Testing the application if it is working or not:
____________________________________________________________________________________________________________________
For testing the application, we would send a CURL request to the URL. We would keep track of the response code sent back. If the response code is 200, that means our application is working fine.
For creating the Job for testing the files:
- Select new item option from the Jenkins menu.
- Assign a name to the Job ( eg. files_test )and select it to be a Freestyle project.
- From the Configure Job option, we set the configurations.
- From the Build Triggers section, we select Build after other projects are built and mention files_classification as the project to watch. This is called a DownStreaming Job.
- In the Build Section, we type the following script:
```
export status=$(curl -o /dev/null -s -w "%{http_code}" http://192.123.32.2932:8080/index.html)

if [[ $status==200 ]]
then
  exit 0
else
  curl --user "admin:admin" http://192.123.32.2932:8080/view/Mlops-project-2/job/files_notify/build?token=file_notification
  exit 1
fi
```
- On clicking the Save option, we add the Job to our Job List.
`Thus, we have successfully tested our application that is running or not.`
____________________________________________________________________________________________________________________
2.4. Job-4: Notifying the Developer if Application not Working:
____________________________________________________________________________________________________________________
If the response code obtained from JOB#3 is not ‘200’, a mail is automatically sent to the user confirming the action.
For creating the Job for Notifying the developer:

1. Select new item option from the Jenkins menu.
2. Assign a name to the Job ( eg. files_notify)and select it to be a Freestyle project.
3. From the Configure Job option, we set the configurations.
4. From the Build Triggers section, we select Trigger builds remotely an option.
5. Provide an Authentication Token
6. In the Build Section, we type the following script:
```
sudo cp -rf /root/Desktop/files/ *
sudo python3 sendmail.py
```

7. On clicking the Save option, we add the Job to our Job List.
Thus, the Job has been setup. To Trigger the Build, the following command would run the job:
`curl --user "<username>:<password>" JENKINS_URL/view/Mlops-project-2/job/files_notify/build?token=TOKEN_NAME`
e.g. `curl --user "admin:admin" http://192.123.32.2932:8080/view/Mlops-project-2/job/files_notify/build?token=file_notification`

We use this Remote Trigger in Job#3 when we don't receive a ‘200’ response code.
____________________________________________________________________________________________________________________
2.5. Job-5: Additional Monitoring Job:
____________________________________________________________________________________________________________________
If the container where the app is running, fails due to any reason then this job will automatically start the container.
For monitoring the Jobs created:
1. Select a new item option from the Jenkins menu.
2. Assign a name to the Job ( eg. monitor_job )and select it to be a Freestyle project.
3. From the Configure Job option, we set the configurations.
4. From the Build Triggers section, we select Build after other projects are built and mention files_classfication as the project to watch.
`It is important to select “Trigger even if the build fails” option from the drop-down list.`
5. In the Build Section, we type the following script:
```
if ! sudo docker ps | grep apache:v1
then
  sudo docker container run -dit -p 85:80 -v /root/Desktop/files/php:/usr/local/apache2/htdocs/  --name php_container apache:v1
fi
```
6. From the Post Build Actions dropdown, we select “Build Other Projects” and mention files_classficationas the project to build.
7. On clicking the Save option, we add the Job to our Job List.

____________________________________________________________________________________________________________________
### Author:
----------------------------------
```diff
+ Vedant Shrivastava | vedantshrivastava466@gmail.com
```
