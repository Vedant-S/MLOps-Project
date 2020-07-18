# A Python program for sending email

import smtplib
import urllib.request as urllib
# Senders email
sender_email = "#"
# Receivers email
rec_email = "#"

message = "Congratulations. The best model has been created."
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("#Username", "#Password")
print("Logged in Successfully!")
# Send Email
server.sendmail("Avik", {rec_email}, message)
print(f"Email has been sent successfully to {rec_email}")
