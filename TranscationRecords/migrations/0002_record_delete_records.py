# Generated by Django 4.0 on 2023-03-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TranscationRecords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(null=True)),
                ('receipt', models.CharField(max_length=6, null=True)),
                ('server', models.CharField(max_length=10, null=True)),
                ('amount', models.CharField(max_length=10, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Records',
        ),
    ]
