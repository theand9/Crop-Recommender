# Generated by Django 2.1.3 on 2019-03-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_auto_20190309_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerregistration',
            name='phoneNumber',
            field=models.IntegerField(unique=True),
        ),
    ]
