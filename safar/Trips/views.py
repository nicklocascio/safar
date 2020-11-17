from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip, Day, DayAction, trip_lib
from django.contrib.auth.models import User
import json
# from .forms import NewTripForm
# Create your views here.

def Trips(request):
	return HttpResponse('Trips page')

def trips_created(request):
	trips = Trip.objects.all()
	trip_starts = list()

	for trip in trips:
		trip_starts.append(trip.start_location)

	response_html = '<br>'.join(trip_starts)

	return HttpResponse(response_html)

def create_trip(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			data = json.loads(request.body.decode('utf-8'))
			user = request.user


			#check if trip already exists. target_trip = instance if so; else None
			user_trips = trip_lib.user_trips(user)
			target_trip = None

			for trip in user_trips:
				if trip.start_location == data['start_location']:
					if trip.destination == data['destination']:
						if trip.days == data['days']:
							target_trip = trip
							break

			if target_trip == None: #no trip, create one
				target_trip = trip_lib.add_trip(user=user, days=data['num_days'])
				trip_lib.edit_trip(trip=trip, start_location=data['start_location'], destination=data['destination'])

			else: #trip exists, edit it
				trip_lib.edit_trip(trip=target_trip, start_location=data['start_location'], destination=data['destination'], days=data['num_days'])

			#update trip day_actions atm
			back_days = [Day.objects.filter(trip=trip)]
			for i in range(data['num_days']):
				if i in data:
					front_day_actions = data[i]
					back_day_actions = [DayAction.objects.filter(day=back_days[i])]

					for i in range(len(front_day_actions)):
						if i < len(back_day_actions):
							edit_action(action=back_day_actions[i], action_def=front_day_actions[i]['action_desc'], action_time=front_day_actions[i]['action_time'])
				else:
					action = trip_lib.add_action(back_day_actions[i])
					trip_lib.edit_action(action=action, action_def=front_day_actions[i]['action_desc'], action_time=front_day_actions[i]['action_time'])




			d = {
				'user':str(user),
				'trip':str(target_trip),
				'start_location':target_trip.start_location,
				'destination':target_trip.destination,
			}

			print(d)

			return render(request, 'directions.html', d)

		else:
			return render(request, 'directions.html', {})
	else:
		data = {}
		if request.method == 'POST':	
			data = json.loads(request.body.decode('utf-8'))
			return render(request, 'directions.html', data)
		else:
			return render(request, 'directions.html', {'hi': 'there'})
		
