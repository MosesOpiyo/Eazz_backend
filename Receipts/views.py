from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from Mpesa.credentials import MpesaAccessToken, LipanaMpesaPpassword
from decouple import config

import json

from .serializers import *
from .models import *

from Mpesa.credentials import LipanaMpesaPpassword

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def receipt_view(request):
    receipt_serializer = ReceiptSerializers(data=request.data)
    data = {}
    if receipt_serializer.is_valid():
        receipt_serializer.save()
        data = receipt_serializer.data['id']
        receipt = Receipt.objects.get(id=receipt_serializer.data['id'])
        print(request.user)
        statement = Statement.objects.create(
            receipt = receipt,
            client = request.user.username,
            code = request.user.id
        )
        statement.save()
        access_token = MpesaAccessToken.validated_mpesa_access_token
        print('Payment processing')
        api_url = config('SAF_STK_PUSH_API')
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": receipt_serializer.data['total'],
            "PartyA": request.user.phone_number,
            "PartyB": int(receipt_serializer.data['till_number']),
            "PhoneNumber": request.user.phone_number,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Account",
            "TransactionDesc": "Testing stk push"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def get_receipts(request):
    data = {}
    receipt = Receipt.objects.all()
    data =  GetReceiptSerializers(receipt,many=True).data
    return Response(data,status = status.HTTP_200_OK)

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def get_user_receipts(request,id):
    data = {}
    receipts = Receipt.objects.get(id=id)
    data =  GetReceiptSerializers(receipts).data
    return Response(data,status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_statements(request):
    data = {}
    statements = Statement.objects.filter(code=request.user.id).order_by("-id")
    data =  GetStatementsSerializers(statements,many=True).data
    return Response(data,status = status.HTTP_200_OK)

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def latest_statements(request):
    data = {}
    statements = Statement.objects.filter(code=request.user.id).latest("id")
    data =  GetStatementsSerializers(statements).data
    return Response(data,status = status.HTTP_200_OK)
    
      
