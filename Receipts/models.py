from django.db import models
import binascii
import os
from datetime import date

from Authentication.models import Account

class Item(models.Model):
    name = models.TextField(null=True)
    item_number = models.IntegerField(null=True) 
    price = models.IntegerField(null=True)
    def __str__(self):
       return self.name
    
class Receipt(models.Model):
    receipt_number = models.CharField(max_length=12,null=True)
    server_name = models.CharField(max_length=40,null=True)
    server = models.CharField(max_length=20,null=True)
    till_number = models.IntegerField(null=True)
    store_name = models.CharField(max_length=100,null=True)
    total = models.IntegerField(null=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return str(self.receipt_number)

class Statement(models.Model):
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,null=True)
    client = models.TextField(null=True)
    code = models.IntegerField(null=True)
    
    def __str__(self):
        return self.client
