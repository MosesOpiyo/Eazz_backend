from django.db import models
import binascii
import os

from Authentication.models import Account

class Items(models.Model):
    name = models.TextField(null=True)
    quantity = models.CharField(max_length=3,null=True) 
    amount = models.CharField(max_length=10,null=True)
    def __str__(self):
       return self.name

class Receipts(models.Model):
    receipt_number = models.CharField(max_length=6,null=True)
    server = models.CharField(max_length=10,null=True) 
    items = models.ManyToManyField(Items)

    def __str__(self):
        return self.receipt_number
    
    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = self.generate_number()
        return super().save(*args, **kwargs)
    
    @classmethod
    def generate_number(cls):
        return binascii.hexlify(os.urandom(6)).decode()
    




