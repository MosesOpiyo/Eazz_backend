from rest_framework import serializers
from .models import Record

class ReceordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['receipt','server','amount']

    def save(self,request):
       record = Record(customer_id=request.user.id,receipt=self.validated_data['receipt'],server=self.validated_data['server'],amount=self.validated_data['amount'])
       record.save()
       return record
    
class GetRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'