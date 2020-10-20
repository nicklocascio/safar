from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip, Day, DayAction, trip_lib
from .forms import NewTripForm
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

def new_trip(request, pk):
	
	if request.method == 'POST':
		form = NewTripForm(request.POST)
		if form.is_valid():
			trip_form = form.save(commit=False)

			


			#post = Post.objects.create(
				#message=form.cleaned_data.get('message'
