# Generated by Django 2.1.7 on 2019-03-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0031_auto_20190327_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmersearch',
            name='aadharNumber',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
