from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import *
from .models import *
from .sms import smsVerification


@api_view(['POST'])
def registration_view(request):
    account_serializer = PhoneSerializer(data=request.data)
    data = {}

    if account_serializer.is_valid():
        account = account_serializer
        number = account.data['phone_number']
        account = Account.objects.filter(phone_number=number)
        if account:
            user_account = Account.objects.get(phone_number=number)
            user_code = Code.objects.get(user = user_account)
            smsVerification(number,user_code.verification_code)
            data['response'] = f"User has been logged in under {user_account.phone_number}"
            return Response(data,status = status.HTTP_200_OK)
        else:
            print("User does not exist.")
            Account.objects.create(phone_number=number)
            new_account = Account.objects.get(phone_number=number)
            new_code = Code.objects.get(user = new_account)
            smsVerification(number,new_code.verification_code)
            data['response'] = f"User has been registered and logged in under {new_account.phone_number}"
            return Response(data,status = status.HTTP_201_CREATED)
        
    else:
        data = account_serializer.errors
        return Response(data,status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verification_view(request):
    code_serializer = CodeSerializer(data=request.data)
    data = {}

    if code_serializer.is_valid():
        user_code = code_serializer
        user_number = user_code.data['phone_number']
        verify_code = user_code.data['code']
        user = Account.objects.get(phone_number=user_number)
        user_code = Code.objects.get(user=user) 
        if verify_code == user_code.verification_code:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key})
        elif verify_code != user_code.verification_code:
            data['error'] = "Verification code did not match account."
            return Response(data,status = status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def username_view(request):
    username_serializer = UsernameSerializer(data=request.data)
    data = {}

    if username_serializer.is_valid():
        user = username_serializer
        user_name = user.data['username']
        user = Account.objects.get(phone_number=request.user.phone_number)
        user.username = user_name
        user.save()
        data['success'] = f"Username {user.username}, added."
    return Response(data,status = status.HTTP_200_OK)
        
        

@api_view(['GET'])
def get_profile(request):
    data = {}
    account = Code.objects.get(user=request.user)
    data =  ProfileSerializer(account).data
    return Response(data,status = status.HTTP_200_OK)



