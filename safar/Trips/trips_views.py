from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Trips(request):
	return HttpResponse('Trips page')


