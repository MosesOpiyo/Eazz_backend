# Generated by Django 4.0 on 2023-02-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Receipts', '0001_initial'),
        ('Authentication', '0007_account_username_delete_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(max_length=10, null=True)),
                ('amount', models.CharField(max_length=10, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.account')),
                ('receipt', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Receipts.receipts')),
            ],
        ),
    ]