from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.core.mail import send_mail
from Trips.models import *

# Create your views here.
def display_user(request):
    users = User.objects.values()
    return render(request, 'display_users.hmtl', {'users': users})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def accountPage(request):
    user = request.user

    trips = list(Trip.objects.filter(user=user))
    print(trips)

# trip.start_location
# trip.destination
# trip.total_time
# trip.days
# trip.uuid

    #for trip in trips:
    #    tripDict = {}
    #    tripDict['start'] = trip.start_location

    return render(request, 'user_account.html', {'trips': trips})
