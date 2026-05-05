#Plaintext email over SSL

import smtplib
import ssl
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

#Constants
SENDER = os.getenv("SENDER")
RECIEVER = os.getenv("RECIEVER")
APP_PASSWORD = os.getenv("APP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("SSL_PORT"))


now = datetime.now()
timestamp = now.strftime("%A %H:%M:%S")

context = ssl.create_default_context()
message = """\
From: {}
To: {}
Subject: CATI dashboard notification

ICT Daybatch completed on {}

Regards,
DCU tools
""".format(SENDER, RECIEVER, timestamp)

with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context = context) as server:
    server.login(SENDER, APP_PASSWORD)
    server.sendmail(SENDER, RECIEVER, message)