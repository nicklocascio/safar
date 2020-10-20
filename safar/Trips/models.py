from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Trip(models.Model):
	start_location = models.CharField(max_length=30, default="here")
	destination = models.CharField(max_length=30, default="there")
	total_time = models.IntegerField(default=0)
	days = models.IntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

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

	def add_trip(user_n, days=1):
		temp_t = Trip(user=user_n, days=days)
		temp_t.save()
		
		for _ in range(days):
			add_day(temp_t)
		
		temp_t.save()
		return temp_t

	def add_day(trip_n):
		temp_d = Day(trip=trip_n)
		temp_d.save()
		add_action(temp_d)
		temp_d.save()
		return temp_d

	def add_action(day_n):
		temp_a = DayAction(day=day_n)
		temp_a.save()
		return temp_a

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







'''
	def create_trip(trip_user, start_location, destination, days, total_time):
	
		trip = Trip.objects.create(start_location=start_location, destination=destination, days=days, total_time=total_time, trip_user=trip_user)
		trip.trip_user = trip_user
		trip.save()

		for _ in range(days):
			Day.objects.create()

		trip.save()

		
'''


'''
	def edit_trip(self, start_location=None, destination=None, days=None, total_time=None):
		if start_location != None:
			self.start_location = start_location
		if destination != None:
			self.destination = destination
		if total_time != None:
			self.total_time = total_time
		if days != None:
			self.days = days
'''

'''
	def create_day(related_id, start_location="", destination="", total_day_time=0):
		day1 = Day.objects.create(start_location=start_location, destination=destination, total_day_time=total_day_time, day_trip=related_id)
		day1.save()
'''
'''

	def get_itinerary():
'''



class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)



