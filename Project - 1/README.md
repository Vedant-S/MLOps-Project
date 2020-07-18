# MLOps Project-1:
____________________________________________________________________________________________________________________
### Integrating Machine Learning with DevOps `(MLops)`:
____________________________________________________________________________________________________________________
### PROBLEM STATEMENT:
- Create container image that’s has Python3 and Keras or numpy installed using dockerfile.
- When we launch this image, it should automatically starts train the model in the container.
- Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins.
```
Job1 : Pull the Github repo automatically when some developers push repo to Github.
Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).
Job3 : Train your model and predict accuracy or metrics.
Job4 : if metrics accuracy is less than 80% , then tweak the machine learning model architecture.
Job5 : Retrain the model or notify that the best model is being created.
```
- Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left.
____________________________________________________________________________________________________________________
### Pre-Requisites:
- Base OS in my case it is Windows 10 and On the Top of Windows 10 I am using Red Hat Enterprise Linux (RHEL 8 ) with the Help of Oracle Virtual Box
- Inside Rhel we need some setup to be ready like we need docker , Jenkins , centos image like I am using centos latest and and using that image I have created one Dockerfile by installing some required python modules like tensorflow , keras , numpy , pillow etc. and we need git to be installed in RHEL8
- And for this work weight need to disable some security in RHEL 8 like firewall
____________________________________________________________________________________________________________________
### Description:
1. Build Docker images for Keras and sklearn installed using Dockerfile:
Using RedHat Linux as base OS, I created two DockerFiles for creating docker images.
- Dockerfile for mlops (Keras) model
- Dockerfile for sklearn models
- To build these image use-
```
docker build -t mlops:v1
docker build -t sklearn:v1
```
- To check the Docker images use:
```
docker images
```
2. Create Local repositories in GitBash and push to GitHub.
Using GitBash from Windows OS create local repository and connect it to GitHub without initializing it.
- Post Commit:
3. Connect Jenkins With GitHub
Launch Jenkins in RedHat and and set web hooks.
- JOB1: pulling the Github repo automatically when some developers push repo to Github.
- JOB2: By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training(ex. In my case I m using CNN, then Jenkins will start the container that has already installed all the softwares required for the cnn processing Tensorflow, Keras).
- JOB3: Train your model and predict accuracy or metrics.And will mail the output. This job will Run after the succesfull build of job2 and if not then it will notify every status to the slack channel. in this job 3 it will check the accuracy if the accuracy is about 95% then it will trigger job4 and notify your model is ready.If accuracy is less than 95% then it will retrain the model and automatically add the layers and epochs .And then go to job4 and notify that the model is trained.
- JOB4 : It will send the mail and also notify that the job is now complete.
- Job 5 : If the job2 or job3 fail or the OS crash or model training stops , then it will again start the container from where the process has stopped.Also send the mail and notify the fail of OS and model.
4. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins.
____________________________________________________________________________________________________________________
### Author:
----------------------------------
```diff
+ Vedant Shrivastava | vedantshrivastava466@gmail.com
```
