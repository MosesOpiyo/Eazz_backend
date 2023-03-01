from django.db import models
from Authentication.models import Account
from Receipts.models import Receipt
import binascii
import os

class Record(models.Model):
    customer_id = models.IntegerField(null=True)
    receipt = models.CharField(max_length=6,null=True)
    server = models.CharField(max_length=10,null=True)
    amount = models.CharField(max_length=10,null=True)
    date = models.DateField(auto_now=True,null=True)

    def __str__(self):
        return self.amount
