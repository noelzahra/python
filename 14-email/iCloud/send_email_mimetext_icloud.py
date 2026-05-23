#icloud MIME email over TLS

import smtplib 
from dotenv import load_dotenv
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

now = datetime.now()
day = now.strftime("%a, %d-%b-%Y")
timestamp = now.strftime("%d-%b-%Y, %H:%M:%S")
user = RECIPIENT_EMAIL.split("@")[0].capitalize()

message = MIMEMultipart('alternative')

message['Subject'] = "Daybatch Notification"
message['From'] = SENDER_EMAIL
message['To'] = RECIPIENT_EMAIL

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

with smtplib.SMTP(SMTP_SERVER, PORT) as server:
    try:
        server.starttls() #upgrade to secure connection
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()