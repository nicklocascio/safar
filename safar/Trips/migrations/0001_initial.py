# Generated by Django 3.1.2 on 2020-10-20 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('total_day_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('total_time', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('itinerary', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='trip_itin', to='Trips.day')),
            ],
        ),
    ]
