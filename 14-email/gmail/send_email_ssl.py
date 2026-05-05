#SMTP library SSL connection use port 465

import os
import smtplib
import ssl
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

#Constants
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("SSL_PORT"))
SENDER = os.getenv("SENDER")
APP_PASSWORD = os.getenv("APP_PASSWORD")

context = ssl.create_default_context()
now = datetime.now()


with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context = context) as server:
    server.login(SENDER, APP_PASSWORD)
    print(f"Worked on {now.strftime('%A, %H:%M:%S')}")