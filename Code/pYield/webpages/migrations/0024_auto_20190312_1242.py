# Generated by Django 2.1.7 on 2019-03-12 07:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0023_auto_20190311_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerregistration',
            name='aadhar_Number',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(15)]),
        ),
    ]
