from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Friend, user_lib

# Create your views here.

def Users(request):
	return HttpResponse('Users page')
