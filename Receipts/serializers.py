from rest_framework import serializers
from Authentication.models import Account

from .models import Item,Receipt,Statement
from Authentication.serializers import UserSerializer

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class ReceiptSerializers(serializers.ModelSerializer):
    items = ItemsSerializers(many=True)
    class Meta:
        model = Receipt
        fields = "__all__"

    def create(self,validated_data):
        item_data = validated_data.pop('items')
        receipt = Receipt.objects.create(**validated_data)
        for item_data in item_data:
          items = Item.objects.create(
            name = item_data.get('name'),
            item_number = item_data.get('item_number'),
            price = item_data.get('price')
          )
          receipt.items.add(items)
        receipt.save()
        return receipt


class GetReceiptSerializers(serializers.ModelSerializer):
    items = ItemsSerializers(many=True)
    class Meta:
        model = Receipt
        fields = "__all__"

class GetStatementsSerializers(serializers.ModelSerializer):
    receipt = GetReceiptSerializers()
    class Meta:
        model = Statement
        fields = ['receipt']