from django.db import models

# Create your models here.



class Trip(models.Model):
	start_location = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	total_time = models.IntegerField(default=0)
	days = models.IntegerField(default=0)

	def __init__(self, start_location, destination, days, total_time):
	
		self.start_location=start_location
		self.destination=destination
		self.days=days
		self.total_time=total_time

		for _ in range(days):
			Day(self.id)
		self.save()


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


class Day(models.Model):
	start_location = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	total_day_time = models.IntegerField(default=0)
	trip_itin = models.ForeignKey(Trip, default="", on_delete=models.CASCADE)
	
	def __init__(self, related_name):
		self.start_location=None
		self.destination=None
		self.total_day_time=0
		self.related_name = related_name

'''
class DayAction(models.Model):
	action_def = models.CharField(max_length=200, default="")
	action_time = models.CharField(max_length=200, default="")
	day_itin = models.ForeignKey(Day, related_name="day_itin", default="", on_delete=models.CASCADE)'''

'''

	def get_itinerary():
'''
