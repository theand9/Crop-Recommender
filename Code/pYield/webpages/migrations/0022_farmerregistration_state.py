# Generated by Django 2.1.7 on 2019-03-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0021_delete_farmerrequeteddetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerregistration',
            name='state',
            field=models.CharField(default='MAHARASHTRA', max_length=20),
        ),
    ]
