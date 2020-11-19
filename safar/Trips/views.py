from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip, Day, DayAction, trip_lib
from django.contrib.auth.models import User
import json
from django.core.serializers.json import DjangoJSONEncoder
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
			print(data)
			user = request.user


			#check if trip already exists. target_trip = instance if so; else None
			target_trip = None
			if 'uuid' in data:
				trip = Trip.objects.filter(uuid=data['uuid'])
				target_trip = trip[0]
			

			if target_trip == None: #no trip, create one
				print('Creating new trip...')
				target_trip = trip_lib.add_trip(user, int(data['num_days']))
				trip_lib.edit_trip(trip=target_trip, start_location=data['start_location'], destination=data['destination'], total_time=data['total_time'])

			else: #trip exists, edit it
				print('Editing trip...')
				trip_lib.edit_trip(trip=target_trip, start_location=data['start_location'], destination=data['destination'], days=data['num_days'], total_time=data['total_time'])

			#update trip day_actions atm
			back_days = list(Day.objects.filter(trip=target_trip))
			for i in range(1, int(target_trip.days)+1):
				print(i)
				if str(i) in data:
					print('Day', i, 'is in data...')
					front_day_actions = data[str(i)]
					back_day_actions = list(DayAction.objects.filter(day=back_days[i-1]))

					for j in range(len(front_day_actions)):
						if j < len(back_day_actions):
							print('Editing Action', j, 'in Day', i)
							trip_lib.edit_action(action=back_day_actions[j], action_def=front_day_actions[j]['action_desc'], action_time=front_day_actions[j]['action_time'])
						else:
							action = trip_lib.add_action(front_day_actions[j])
							trip_lib.edit_action(action=action, action_def=front_day_actions[j]['action_desc'], action_time=front_day_actions[j]['action_time'])
				else:
					print('Day', i, 'is NOT in data... adding day')
					trip_lib.add_day(target_trip)


			

			d = {
				'user':str(user),
				'uuid':str(target_trip),
				'start_location':target_trip.start_location,
				'destination':target_trip.destination,
				'total_time': target_trip.total_time,
			}

			for i in range(1, int(target_trip.days)+1):
				print('Day', i)
				back_day_action = list(DayAction.objects.filter(day=back_days[i-1]))
				d[str(i)] = list()

				for j in range(len(back_day_action)):
					if j >= 0:
						print('Adding action', j, 'in Day', i)
						d[str(i)].append({})
						d[str(i)][j]['action_desc'] = back_day_action[j].action_def
						d[str(i)][j]['action_time'] = back_day_action[j].action_time

			print(d)
			my_data = json.dumps(d)

			return render(request, 'directions.html', {'my_data': my_data})

		else:
			return render(request, 'directions.html', {})
	else:
		data = {}
		if request.method == 'POST':	
			data = json.loads(request.body.decode('utf-8'))
			return render(request, 'directions.html', data)
		else:
			return render(request, 'directions.html', {'hi': 'there'})
		
