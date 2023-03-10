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
        data =  GetReceiptSerializers(request.data).data
        return Response(data,status=status.HTTP_201_CREATED)

    else:
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET']) 
def get_receipts(request):
    data = {}
    receipt = Receipts.objects.all()
    data =  GetReceiptSerializers(receipt,many=True).data
    return Response(data,status = status.HTTP_200_OK)

   
    
      
