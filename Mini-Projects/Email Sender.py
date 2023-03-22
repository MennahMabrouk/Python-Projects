#Email Sender

from email.message import EmailMessage
#Needed Library
import ssl
import smtplib

#Put your E-mail
email_sender = "" 
#Put your Generated Password
email_password = ""
#Put Other E-mail
email_recevier = ""


subject = "Friends" #This is an e.g write what you want
body = "Love you my friend" #This is an e.g write what you want

emailmessage = EmailMessage()
emailmessage['From'] = email_sender
emailmessage['To'] = email_recevier
emailmessage['Subject'] = subject

emailmessage.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context ) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recevier, emailmessage.as_string())

