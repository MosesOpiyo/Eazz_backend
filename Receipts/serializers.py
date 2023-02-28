from rest_framework import serializers

from .models import Items,Receipts
from Authentication.serializers import UserSerializer

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name','quantity','amount']


class ReceiptSerializers(serializers.ModelSerializer):
    items = ItemsSerializers(many=True)
    class Meta:
        model = Receipts
        fields = '__all__'

    def create(self,validated_data):
        item_data = validated_data.pop('items')
        receipt = Receipts.objects.create(**validated_data)
        for item_data in item_data:
          items = Items.objects.create(
            name = item_data.get('name'),
            quantity = item_data.get('quantity'),
            amount = item_data.get('amount')
          )
          receipt.items.add(items)
        receipt.save()
        return receipt


class GetReceiptSerializers(serializers.ModelSerializer):
    items = ItemsSerializers(many=True)
    class Meta:
        model = Receipts
        fields = ['receipt_number','server','items']
