from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.



class Trip(models.Model):
	start_location = models.CharField(max_length=30, default="here")
	destination = models.CharField(max_length=30, default="there")
	total_time = models.IntegerField(default=0)
	days = models.IntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)


	def __str__(self):
		return str(self.uuid)

class Day(models.Model):
	start_location = models.CharField(max_length=30, default="here")
	destination = models.CharField(max_length=30, default="there")
	total_day_time = models.IntegerField(default=0)
	trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

class DayAction(models.Model):
	action_def = models.CharField(max_length=200, default="")
	action_time = models.CharField(max_length=200, default="")
	day = models.ForeignKey(Day, on_delete=models.CASCADE)

class trip_lib():


	def user_trips(user_n):
		return list(Trip.objects.filter(user=user_n))
		


	def add_action(day_n):
		temp_a = DayAction(day=day_n)
		temp_a.save()
		return temp_a

	def add_day(trip_n):
		temp_d = Day(trip=trip_n)
		temp_d.save()
		trip_lib.add_action(temp_d)
		temp_d.save()
		return temp_d

	def add_trip(user_n, days=1):
		temp_t = Trip(user=user_n, days=days)
		temp_t.save()
		
		for _ in range(days):
			trip_lib.add_day(temp_t)
		
		temp_t.save()
		return temp_t


	def edit_trip(trip=None, start_location="", destination="", total_time=0, days=0, user=None):
		if trip != None: 
			if start_location != "":
				trip.start_location = start_location
			if destination != "":
				trip.destination = destination
			if total_time != 0:
				trip.total_day_time = total_day_time
			if days != 0:
				trip.days = days
			if user != None:
				trip.user = user

			trip.save()
		return

	def edit_day(day=None, start_location="", destination="", total_day_time=0, trip=None):
		if day != None:
			if trip != None:
				day.trip = trip
			if start_location != "":
				day.start_location = start_location
			if destination != "":
				day.destination = destination
			if total_day_time != 0:
				day.total_day_time = total_day_time

			day.save()
		return

		
	def edit_action(action=None, action_def="", action_time=0, day=None):
		if action != None:
			if action_def != "":
				action.action_def = action_def
			if action_time != 0:
				action.action_time = action_time
			if day != None:
				action.day = day
			
			action.save()

		return


