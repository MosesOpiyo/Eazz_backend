from twilio.rest import Client
from dotenv import load_dotenv
import os

TWILIO_ACCOUNT_SID = str(os.getenv('TWILIO_ACCOUNT_SID'))
TWILIO_AUTH_TOKEN = str(os.getenv('TWILIO_AUTH_TOKEN'))

def smsVerification(client_number,client_code):
    account_sid = "AC65209008165d3586d586276d472b6dc4"
    auth_token = "fde635b77ac2331654b52138723fa375"
    client = Client(account_sid,auth_token)

    message = client.messages \
                    .create(
                        body=f"Your Eazz Verification code is {client_code}",
                        from_="+13149474262",
                        to=client_number
                )