# Generated by Django 4.0 on 2023-03-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0031_rename_items_item_rename_receipts_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]