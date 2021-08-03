import sys
import os
import django
from twilio.rest import Client 
from twilio.twiml.messaging_response import MessagingResponse
import environ

sys.path.append(os.getcwd())
os.environ["DJANGO_SETTINGS_MODULE"] = "emblazEX.settings"
django.setup()

env = environ.Env()
environ.Env.read_env()

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
def fetch_response():
    return client.messages.list(from_ = TWILIO_NUMBER)


def post_message(username, number, body):
    msg = client.messages.create(
        to = number,
        from_ = TWILIO_NUMBER,
        body = f"{body}  (from:{username})"
    )
    return True