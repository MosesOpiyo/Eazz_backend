from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import *
from .models import *

@api_view(['POST'])
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
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET']) 
def get_receipts(request):
    data = {}
    receipt = Receipt.objects.all()
    data =  GetReceiptSerializers(receipt,many=True).data
    return Response(data,status = status.HTTP_200_OK)

@api_view(['GET']) 
def get_user_receipts(request,id):
    data = {}
    receipts = Receipt.objects.get(id=id)
    data =  GetReceiptSerializers(receipts).data
    return Response(data,status = status.HTTP_200_OK)

@api_view(['GET']) 
def get_statements(request):
    data = {}
    statements = Statement.objects.filter(code=request.user.id)
    data =  GetStatementsSerializers(statements,many=True).data
    return Response(data,status = status.HTTP_200_OK)

   
    
      
