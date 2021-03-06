# Generated by Django 3.1.2 on 2020-10-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0009_day_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='destination',
            field=models.CharField(default='there', max_length=30),
        ),
        migrations.AlterField(
            model_name='day',
            name='start_location',
            field=models.CharField(default='here', max_length=30),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(default='there', max_length=30),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_location',
            field=models.CharField(default='here', max_length=30),
        ),
    ]
