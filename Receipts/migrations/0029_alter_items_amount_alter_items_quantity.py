# Generated by Django 4.0 on 2023-02-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0028_alter_items_amount_alter_items_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='amount',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.CharField(max_length=3, null=True),
        ),
    ]