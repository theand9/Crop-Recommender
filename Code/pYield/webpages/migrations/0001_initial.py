# Generated by Django 2.1.3 on 2019-03-09 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmerRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmerName', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('areaInHectare', models.IntegerField()),
                ('aadharNumber', models.IntegerField()),
                ('village_district', models.CharField(max_length=120)),
                ('state', models.TextField(max_length=50)),
            ],
        ),
    ]
