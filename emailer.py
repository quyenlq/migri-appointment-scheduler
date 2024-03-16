import smtplib
from email.mime.text import MIMEText
from envs import *

subject = "Migri notification"
body = "This is the body of the text message"
sender = SENDER
recipients = RECIPIENTS
password = PASSWORD

def send_email(subject=subject, body=body, sender=sender, recipients=recipients, password=password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    print(sender, password)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")