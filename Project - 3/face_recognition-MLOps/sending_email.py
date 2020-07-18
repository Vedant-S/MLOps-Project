# A Python program for sending email

import smtplib
import urllib.request as urllib
# Senders email
sender_email = "kundu.abheek1999@gmail.com"
# Receivers email
rec_email = "kundu.abheek1999@hotmail.com"

message = "Congratulations. The best model has been created."
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("kundu.abheek1999@gmail.com", "avik1234")
print("Logged in Successfully!")
# Send Email
server.sendmail("Avik", "kundu.abheek1999@hotmail.com", message)
print(f"Email has been sent successfully to {rec_email}")
