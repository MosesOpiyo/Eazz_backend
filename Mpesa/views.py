from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . credentials import MpesaAccessToken, LipanaMpesaPpassword
from decouple import config

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def getAccessToken(request):
    consumer_key = config('SAF_CONSUMER_KEY')
    consumer_secret = config('SAF_CONSUMER_SECRET')
    api_URL = config('SAF_ACCESS_TOKEN_API')

    response = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(response.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = config('SAF_STK_PUSH_API')
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": request.user.phone_number,
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": request.user.phone_number,
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Account",
        "TransactionDesc": "Testing stk push"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
    return HttpResponse('success')
