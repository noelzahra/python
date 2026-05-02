#SMTP library TLS connection use port 587

import smtplib
import ssl

from datetime import datetime

#Constants
SMTP_SERVER = "smtp.gmail.com"
PORT = 587 #TLS port
SENDER = "zarafinancial@gmail.com"
APP_PASSWORD = "tglz wtgi pucc vwiv"


context = ssl.create_default_context()
now = datetime.now()

try:
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    server.ehlo()
    server.starttls(context = context)
    server.ehlo()
    server.login(SENDER, APP_PASSWORD)
    print(f"Worked {now.strftime("%A %d-%B-%Y %H:%M:%S")}")
except Exception as e:
    print(e)
finally:
    server.quit()