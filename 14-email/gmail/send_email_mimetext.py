#gmail MIME email over SSL

import smtplib 
import ssl
from dotenv import load_dotenv
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

SENDER = os.getenv("SENDER")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECIEVER = os.getenv("RECIEVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("SSL_PORT"))

#Get current date and time
now = datetime.now()
day = now.strftime("%a, %d-%b-%Y")
timestamp = now.strftime("%d-%b-%Y, %H:%M:%S")

#Email message
message = MIMEMultipart('alternative')

message['Subject'] = "Daybatch Notification"
message['From'] = SENDER
message['To'] = RECIEVER

text = """\
Subject: CATI dashboard notification

ICT Daybatch completed on {}

Regards,
DCU tools
""".format(timestamp) 

html = """
<html>
    <head>
        <style>
            table {
                border-collapse: collapse;
            }
            tr:nth-child(odd){
                background-color: #efefef;
            }
            td{
                border: 1px solid black;
                padding: 8px;
            }
"""  + """</style>
    </head>
    <body>
        <p>Hi,</p>
        <p>ICT Daybatch completed on {}</p>
        <table>
            <tr>
                <td><b>Time</b></td>
                <td><b>Details</b></td>
            </tr>
            <tr>
                <td>{}</td>
                <td>346 cases completed successfully</td>
            </tr>
        </table>
        <p>Have a nice day</p>
    </body>
</html>   
""".format(day, timestamp)

text_message = MIMEText(text, 'plain')
html_message = MIMEText(html, 'html')

message.attach(text_message)
message.attach(html_message) #last attach is preferred one, shown first by browser

context = ssl.create_default_context()

with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
    server.login(SENDER, APP_PASSWORD)
    server.sendmail(SENDER, RECIEVER, message.as_string())