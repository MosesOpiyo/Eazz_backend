from rest_framework import serializers
from Authentication.models import Account

from .models import Item,Receipt
from Authentication.serializers import UserSerializer

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name','quantity','amount']

class ReceiptSerializers(serializers.ModelSerializer):
    items = ItemsSerializers(many=True)
    class Meta:
        model = Receipt
        fields = '__all__'

    def create(request,validated_data):
        item_data = validated_data.pop('items')
        receipt = Receipt.objects.create(
            **validated_data
        )
        for item_data in item_data:
            total_amount =  (item_data.get('quantity') * item_data.get('amount'))
            items = Item.objects.create(
                name = item_data.get('name'),
                quantity = item_data.get('quantity'),
                amount = total_amount,
            )
            
            receipt.items.add(items)
        receipt.save()
        return receipt


class GetReceiptSerializers(serializers.ModelSerializer):
    items = ItemsSerializers(many=True)
    class Meta:
        model = Receipt
        fields = ['id','receipt_number','server','customer_id','customer_name','items']
