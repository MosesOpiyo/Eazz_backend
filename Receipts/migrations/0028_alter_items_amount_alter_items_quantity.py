# Generated by Django 4.0 on 2023-02-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0027_alter_receipts_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]