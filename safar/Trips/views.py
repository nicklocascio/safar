from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip, Day, DayAction, trip_lib
import simplejson as json
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
			trip = trip_lib.add_trip(user)
			trip_lib.edit_trip(trip=trip, start_location=data['start_location'], destination=data['destination'])
			d = {
				'user':str(user),
				'start_location':trip.start_location,
				'destination':trip.destination,
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
			return render(request, 'directions.html', {})
		
