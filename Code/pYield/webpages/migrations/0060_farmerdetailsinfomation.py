# Generated by Django 2.1.7 on 2019-04-12 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0059_auto_20190410_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmerDetailsInfomation',
            fields=[
                ('farmer_Name', models.CharField(max_length=30)),
                ('phone_Number', models.CharField(max_length=10, unique=True)),
                ('areaInHectare', models.CharField(max_length=3)),
                ('aadhar_Number', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=20)),
                ('village', models.CharField(default='', max_length=30)),
                ('date_register', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_year_profit', models.CharField(max_length=20)),
            ],
        ),
    ]