from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import *
from .models import *

@api_view(['POST'])
def transactionRecord_view(request):

    record_serializers = ReceordSerializers(data=request.data)
    data = {}

    if record_serializers.is_valid():
        record_serializers.save(request)
        data = GetRecordSerializers(request.data).data
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        record_serializers.errors 
        return Response(data,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_records(request):
    data = {}
    record = Record.objects.all()
    data =  GetRecordSerializers(record,many=True).data
    return Response(data,status = status.HTTP_200_OK)       
        
