from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('About Page')

def home(request):
    return HttpResponse('<h1><b>SAFAR Home Page</b></h1>')
