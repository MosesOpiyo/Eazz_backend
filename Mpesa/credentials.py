import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64
from decouple import config

class MpesaC2bCredential:
    consumer_key = config('SAF_CONSUMER_KEY')
    consumer_secret = config('SAF_CONSUMER_SECRET')
    api_URL = config('SAF_ACCESS_TOKEN_API')

class MpesaAccessToken:
    response = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(response.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = '174379'
    OffSetValue = '0'
    passkey = config('SAF_PASS_KEY')

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')