# Generated by Django 2.1.3 on 2019-03-09 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_auto_20190309_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmerregistration',
            name='state',
        ),
    ]
