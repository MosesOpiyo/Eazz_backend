# Generated by Django 4.0 on 2023-04-30 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0008_account_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
    ]