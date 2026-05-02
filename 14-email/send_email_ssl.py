#SMTP library SSL connection use port 465

import smtplib, ssl
from datetime import datetime

#Constants
SMTP_SERVER = "smtp.gmail.com"
PORT = 465 #SSL port
SENDER = "zarafinancial@gmail.com"
APP_PASSWORD = "tglz wtgi pucc vwiv"

context = ssl.create_default_context()
now = datetime.now()


with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context = context) as server:
    server.login(SENDER, APP_PASSWORD)
    print(f"Worked on {now.strftime('%A, %H:%M:%S')}")