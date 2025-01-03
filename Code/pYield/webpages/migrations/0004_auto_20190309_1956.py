# Generated by Django 2.1.3 on 2019-03-09 14:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_remove_farmerregistration_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerregistration',
            name='areaInHectare',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='farmerregistration',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='farmerregistration',
            name='village_district',
            field=models.CharField(max_length=100),
        ),
    ]
