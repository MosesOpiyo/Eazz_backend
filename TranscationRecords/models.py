from django.db import models
from Authentication.models import Account
from Receipts.models import Receipts

class Records(models.Model):
    customer = models.OneToOneField(Account,null=True,on_delete=models.CASCADE)
    receipt = models.OneToOneField(Receipts,null=True,on_delete=models.CASCADE)
    server = models.CharField(max_length=10,null=True)
    amount = models.CharField(max_length=10,null=True)
    date = models.DateField(auto_now=True,null=True)
