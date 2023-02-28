# Generated by Django 4.0 on 2023-02-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0005_rename_details_receipts_receipt_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipts',
            name='receipt_details',
        ),
        migrations.AddField(
            model_name='receipts',
            name='receipt_number',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='receipts',
            name='server',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='ReceiptDetails',
        ),
    ]