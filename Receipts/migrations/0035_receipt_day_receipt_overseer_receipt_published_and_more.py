# Generated by Django 4.0 on 2023-04-30 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0034_receipt_server_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='day',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='overseer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='published',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='receipt',
            name='week',
            field=models.IntegerField(null=True),
        ),
    ]
