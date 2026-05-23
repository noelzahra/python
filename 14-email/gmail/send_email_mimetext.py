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
user = RECIEVER.split(".")[0].capitalize()

#Email message
message = MIMEMultipart('alternative')

message['Subject'] = "Daybatch Notification"
message['From'] = SENDER
message['To'] = RECIEVER

text = """\
Subject: CATI dashboard notification

ICT Daybatch completed on {timestamp}

Regards,
DCU tools
"""

html = """
<html>
    <head>
        <style>
            table {{
                border-collapse: collapse;
            }}
            tr:nth-child(odd){{
                background-color: #efefef;
            }}
            td{{
                border: 1px solid black;
                padding: 8px;
            }}
        </style>
    </head>
    <body>
        <p>Hi {user},</p>
        <p>ICT Daybatch completed on {timestamp}</p>
        <table>
            <tr>
                <td><b>Time</b></td>
                <td><b>Details</b></td>
            </tr>
            <tr>
                <td>{timestamp}</td>
                <td>346 cases completed successfully</td>
            </tr>
        </table>
        <p>Have a nice day</p>
    </body>
</html>   
"""

text_message = MIMEText(text, 'plain')
html_message = MIMEText(html, 'html')

message.attach(text_message)
message.attach(html_message) #last attach is preferred one, shown first by browser

context = ssl.create_default_context()

with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
    try:
        server.login(SENDER, APP_PASSWORD)
        server.sendmail(SENDER, RECIEVER, message.as_string())
        print(f"Email sent successfully to: {RECIEVER}")
    except Exception as e:
        print(e)
    finally:
        server.quit()