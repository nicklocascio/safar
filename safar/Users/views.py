from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

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

@login_required
def accountPage(request):
    context = {'UserTrips': {'Trip 1': {'Start Location': 'Detroit', 'Destination': 'South Bend', 'Drive Time': '3 Hours', 'Days': '1 Day'}, 
                             'Trip 2': {'Start Location': 'Miami', 'Destination': 'Chicago', 'Drive Time': '16 Hours', 'Days': '3 Days'}, 
                             'Trip 3': {'Start Location': 'Los Angeles', 'Destination': 'Portland', 'Drive Time': '14 Hours', 'Days': '3 Days'},
                             'Trip 4': {'Start Location': 'New York City', 'Destination': 'Nashville', 'Drive Time': '9 Hours', 'Days': '2 Days'},
                             'Trip 5': {'Start Location': 'Austin', 'Destination': 'Phoenix', 'Drive Time': '20 Hours', 'Days': '4 Days'},
                             'Trip 6': {'Start Location': 'Austin', 'Destination': 'Phoenix', 'Drive Time': '20 Hours', 'Days': '4 Days'},
                             'Trip 7': {'Start Location': 'Austin', 'Destination': 'Phoenix', 'Drive Time': '20 Hours', 'Days': '4 Days'},
                             'Trip 8': {'Start Location': 'Austin', 'Destination': 'Phoenix', 'Drive Time': '20 Hours', 'Days': '4 Days'},
                             'Trip 9': {'Start Location': 'Austin', 'Destination': 'Phoenix', 'Drive Time': '20 Hours', 'Days': '4 Days'},
                             'Trip 10': {'Start Location': 'Austin', 'Destination': 'Phoenix', 'Drive Time': '20 Hours', 'Days': '4 Days'},
                            }
              }
    return render(request, 'user_account.html', context)
