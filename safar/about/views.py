from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request, 'about_custom.html')

def home(request):
    return render(request, 'index.html')
