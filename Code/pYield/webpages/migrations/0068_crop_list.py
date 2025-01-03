# Generated by Django 2.1.7 on 2019-04-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0067_rainfall2k19'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=30)),
                ('crop_Arhar', models.IntegerField()),
                ('crop_Bajra', models.IntegerField()),
                ('crop_Cotton', models.IntegerField()),
                ('crop_Gram', models.IntegerField()),
                ('crop_Groundnut', models.IntegerField()),
                ('crop_Jowar', models.IntegerField()),
                ('crop_Maize', models.IntegerField()),
                ('crop_Moong', models.IntegerField()),
                ('crop_Mustard', models.IntegerField()),
                ('crop_Nigerseed', models.IntegerField()),
                ('crop_Ragi', models.IntegerField()),
                ('crop_Rice', models.IntegerField()),
                ('crop_Safflower', models.IntegerField()),
                ('crop_Sesamum', models.IntegerField()),
                ('crop_Soyabean', models.IntegerField()),
                ('crop_Sugarcane', models.IntegerField()),
                ('crop_Sunflower', models.IntegerField()),
                ('crop_Urad', models.IntegerField()),
                ('crop_Wheat', models.IntegerField()),
                ('time_to_Grow', models.IntegerField()),
                ('season', models.CharField(max_length=20)),
            ],
        ),
    ]
