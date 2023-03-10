# Generated by Django 4.0 on 2023-01-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
