# Generated by Django 4.0 on 2023-02-28 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0022_alter_receipts_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipts',
            old_name='customer',
            new_name='user',
        ),
    ]
