"""safar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from about import views as about_views
from Users import views as user_views
from Trips import views as trips_views

urlpatterns = [
    path('signup/', user_views.signup, name='signup'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/', user_views.display_user, name='display_users'),
    path('about/', about_views.about, name='about'),
    path('admin/', admin.site.urls),
	path('', about_views.home, name='index'),
	path('home/', about_views.home, name='index'),
    path('trips/', trips_views.Trips, name='trips'),
    path('trips_create/', trips_views.trips_created, name='trips_created'),
]
