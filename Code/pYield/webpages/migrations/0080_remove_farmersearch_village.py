# Generated by Django 2.2 on 2019-04-15 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0079_auto_20190414_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmersearch',
            name='village',
        ),
    ]
