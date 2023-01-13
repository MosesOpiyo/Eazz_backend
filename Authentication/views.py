from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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
            print(f"The user exists.")
            user_account = Account.objects.get(phone_number=number)
            user_code = Code.objects.get(user = user_account)
            print(f"Existing user is {user_account.phone_number} with code, {user_code.verification_code}")
            data = f"User {user_account.phone_number},{user_code.verification_code} is logged in"
            return Response(data,status = status.HTTP_200_OK)
        else:
            print("User does not exist.")
            Account.objects.create(phone_number=number)
            new_account = Account.objects.get(phone_number=number)
            new_code = Code.objects.get(user = new_account)
            print(f"New user, {new_account.phone_number} has been created with code {new_code.verification_code}")
            data = f"User {new_account.phone_number},{new_code.verification_code} has been created and logged in"
            return Response(data,status = status.HTTP_201_CREATED)
        
    else:
        data = account_serializer.errors
        return Response(data,status = status.HTTP_400_BAD_REQUEST)

 

        
