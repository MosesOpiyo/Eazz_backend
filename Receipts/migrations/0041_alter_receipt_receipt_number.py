# Generated by Django 4.0 on 2023-04-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0040_remove_receipt_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='receipt_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
