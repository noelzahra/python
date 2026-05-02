#Plaintext email over SSL

import smtplib
import ssl
from datetime import datetime

#Constants
SMTP_SERVER = "smtp.gmail.com"
PORT = 465 #SSL port
SENDER = "zarafinancial@gmail.com"
RECIEVER = "noel.zahra@gov.mt"
APP_PASSWORD = "tglz wtgi pucc vwiv"

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