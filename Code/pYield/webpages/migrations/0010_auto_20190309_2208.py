# Generated by Django 2.1.3 on 2019-03-09 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0009_farmerregistration_date_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmerregistration',
            old_name='village_district',
            new_name='district',
        ),
    ]
