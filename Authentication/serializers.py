from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Account,MyAccountManager,Code

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone_number']

    def save(self):
        account = Account(phone_number=self.validated_data['phone_number'])
        account.save()
        return account
        
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','phone_number','date_joined','last_login']

class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=15,
        )
    def get_number(self):
        phone_number = self.validated_data['phone_number']
        return phone_number
class CodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=15,
        )
    code = serializers.CharField(
        max_length=5,
        )
    def get_code(self):
        phone_number = self.validated_data['phone_number']
        code = self.validated_data['code']
        return phone_number,code
