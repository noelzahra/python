#SMTP library TLS connection use port 587

import smtplib
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

#Constants
SENDER = os.getenv("SENDER")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECIEVER = os.getenv("RECIEVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("TLS_PORT"))

now = datetime.now()
message = f"Worked {now.strftime('%A %d-%B-%Y %H:%M:%S')}"

try:
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SENDER, APP_PASSWORD)
    server.sendmail(SENDER, RECIEVER, message)
    print("Email sent successfully!")
except Exception as e:
    print(e)
finally:
    server.quit()