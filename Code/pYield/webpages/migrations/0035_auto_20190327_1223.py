# Generated by Django 2.1.7 on 2019-03-27 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0034_auto_20190327_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmersearch',
            old_name='aadharNumber',
            new_name='Aadhar',
        ),
        migrations.RenameField(
            model_name='farmersearch',
            old_name='farmerName',
            new_name='Farmer',
        ),
        migrations.RenameField(
            model_name='farmersearch',
            old_name='state',
            new_name='State',
        ),
    ]
