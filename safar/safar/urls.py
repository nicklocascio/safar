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
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from about import views as about_views
from Users import views as user_views
from Trips import views as trips_views

urlpatterns = [	
	path('accounts/', include('django.contrib.auth.urls')),                    # account urls
	path('accounts/signup/', user_views.signup, name='signup'),

    path('users/', user_views.display_user, name='display_users'),             

    path('about/', about_views.about, name='about'),                           # about page url

    path('admin/', admin.site.urls),

	path('', about_views.home, name='home'),                                   # homepage urls
	path('home/', about_views.home, name='home'),

    path('trips/', trips_views.Trips, name='trips'),                           # trip urls
    path('trips_create/', trips_views.trips_created, name='trips_created'),

	path('userAccount/', user_views.accountPage, name='user_account'),
]
