from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def display_user(request):
    users = User.objects.all()
    return render(request, 'display_users.hmtl', {'users': users})

def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})