from twilio.rest import Client
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
DCU_PHONE_NUMBER = os.getenv('DCU_PHONE_NUMBER')
CONTENT_SID = os.getenv('CONTENT_SID')


def send_whatsapp(to: str = DCU_PHONE_NUMBER, body: str = None, content_sid: str = CONTENT_SID, content_variables: dict = None) -> str:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    kwargs = {
        "from_": TWILIO_PHONE_NUMBER,
        "to": to,
    }

    if content_sid:
        now = datetime.now().strftime("%A %d/%m/%Y %H:%M:%S")
        default_variables = {
            "name"     :"Noel",
            "payload"     : f"Message sent on {now}"
            }
        kwargs["content_sid"] = content_sid
        kwargs["content_variables"] = json.dumps(content_variables or default_variables)
    elif body:
        kwargs["body"] = body

    message = client.messages.create(**kwargs)
    print(f"Message sent: {message.sid}")
    return message.sid


if __name__ == "__main__":
    send_whatsapp()
