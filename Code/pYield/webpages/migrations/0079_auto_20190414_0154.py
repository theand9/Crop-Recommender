# Generated by Django 2.2 on 2019-04-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0078_delete_crop_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop_List',
            fields=[
                ('crop', models.CharField(max_length=30, primary_key=True, serialize=False)),
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
        migrations.AlterField(
            model_name='seasonencode',
            name='kharif',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seasonencode',
            name='rabi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seasonencode',
            name='wholeYear',
            field=models.IntegerField(),
        ),
    ]
