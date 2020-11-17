from django import forms
from .models import Trip, Day, DayAction, trip_lib

class NewTripForm(forms.ModelForm):
	start_location = forms.CharField(widget=forms.Textarea(), max_length=30)
	destination = forms.CharField(widget=forms.Textarea(), max_length=30)
	total_time = forms.IntegerField(widget=forms.Textarea())
	days = forms.IntegerField(widget=forms.Textarea())
	
	class Meta:
		model = Trip
		fields = ('start_location', 'destination', 'total_time', 'days')
