from twilio.rest import Client
import os

def smsVerification(client_number,client_code):
    account_sid = "AC092a81b764531cae2b1ae5ddcef3bcd9"
    auth_token = "f6a8d50aae590f7c0b9b3646a5abc1c6"
    client = Client(account_sid,auth_token)

    message = client.messages \
                    .create(
                        body=f"Your Eazz Verification code is {client_code}",
                        from_="+16206229068",
                        to=client_number
                )

