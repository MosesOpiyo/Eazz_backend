# Generated by Django 4.0 on 2023-04-30 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0039_alter_receipt_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='customer',
        ),
    ]
