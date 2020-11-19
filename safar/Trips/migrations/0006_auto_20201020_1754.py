# Generated by Django 3.1.2 on 2020-10-20 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0005_auto_20201020_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='trip_user',
        ),
        migrations.AlterField(
            model_name='day',
            name='day_trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_days', to='Trips.trip'),
        ),
    ]