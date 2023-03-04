from django.db import models
import binascii
import os

from Authentication.models import Account

class Item(models.Model):
    name = models.TextField(null=True)
    quantity = models.IntegerField(null=True) 
    amount = models.IntegerField(null=True)
    def __str__(self):
       return self.name

class Receipt(models.Model):
    id = models.AutoField(primary_key=True)
    receipt_number = models.CharField(max_length=6,null=True)
    server = models.CharField(max_length=10,null=True)
    customer_id = models.IntegerField(null=True)
    customer_name = models.CharField(max_length=10,null=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.receipt_number
    
    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = self.generate_number()
        return super().save(*args, **kwargs)
    
    @classmethod
    def generate_number(cls):
        return binascii.hexlify(os.urandom(6)).decode()
    




