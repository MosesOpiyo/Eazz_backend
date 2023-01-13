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
class CodeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model =  Code
        fields = ["verification_code","user"]

    def save(self,request):
        code = Code(verification_code=self.validated_data['verification_code'],user=request.user)
        print(f"Code for {code.user.phone_number},{code.verification_code} has been created.")
        code.save()
        return code
