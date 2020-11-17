# Generated by Django 3.1.2 on 2020-10-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0004_auto_20201020_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='trip_itin',
        ),
        migrations.AddField(
            model_name='day',
            name='day_trip',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_user',
            field=models.CharField(default='', max_length=30),
        ),
    ]
