# Generated by Django 4.0 on 2023-02-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0013_receipts_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipts',
            name='customer',
        ),
    ]
