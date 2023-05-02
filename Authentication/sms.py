from twilio.rest import Client
import os
from decouple import config

def smsVerification(client_number,client_code):
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid,auth_token)

    message = client.messages \
                    .create(
                        body=f"Your Eazz Verification code is {client_code}",
                        from_="+16206229068",
                        to=client_number
                )

