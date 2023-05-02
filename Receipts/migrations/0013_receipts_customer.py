# Generated by Django 4.0 on 2023-02-28 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0007_account_username_delete_username'),
        ('Receipts', '0012_remove_items_receipt_receipts_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipts',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.account'),
        ),
    ]
