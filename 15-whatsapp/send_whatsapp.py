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

now = datetime.now().strftime("%A %d/%m/%Y %H:%M:%S")
timestamp = f"Message sent on {now}"  

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        to =DCU_PHONE_NUMBER,
        content_sid=CONTENT_SID,
        content_variables=json.dumps(
            {
            "1": timestamp
            }
        )
)
print(f"Message content: {message.body}")