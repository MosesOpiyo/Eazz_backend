from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
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
            token, created = Token.objects.get_or_create(user=user_account)
            data['user'] = UserSerializer(user_account).data,{"token":token.key}
            return Response(data,status = status.HTTP_200_OK)
        else:
            print("User does not exist.")
            Account.objects.create(phone_number=number)
            new_account = Account.objects.get(phone_number=number)
            new_code = Code.objects.get(user = new_account)
            smsVerification(number,new_code.verification_code)
            token, created = Token.objects.get_or_create(user=new_account)
            data['user'] = UserSerializer(new_account).data,{"token":token.key}
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
            data = "Account has successfully verified"
            return Response(data,status = status.HTTP_200_OK)
        elif verify_code != user_code.verification_code:
            data = "Verification code did not match account."
            return Response(data,status = status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_404_NOT_FOUND)


        
