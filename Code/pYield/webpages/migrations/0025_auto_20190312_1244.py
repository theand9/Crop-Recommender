# Generated by Django 2.1.7 on 2019-03-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0024_auto_20190312_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerregistration',
            name='aadhar_Number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]