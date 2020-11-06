from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('About Page')

def home(request):
    #return render(request, 'index.html')
	return render(request, 'home.html')
