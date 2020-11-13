from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import requests
from pprint import pprint

mapbox_access_token = 'pk.eyJ1Ijoic2FmYXJ0ZWFtMjAyMCIsImEiOiJja2dtbHRsbW4wMWtlMnhxbDNheGJ6OWY5In0.sQWD2q6skgQK31V-ip2Ltg'

# Create your views here.
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    return render(request, 'default_map.html', {'mapbox_access_token': mapbox_access_token})

def directions(request):
    '''
    request_str = 'https://api.mapbox.com/directions/v5/mapbox/cycling/-104.99,39.739;-86.252,41.676?geometries=geojson&access_token=pk.eyJ1Ijoic2FmYXJ0ZWFtMjAyMCIsImEiOiJja2dtbHRsbW4wMWtlMnhxbDNheGJ6OWY5In0.sQWD2q6skgQK31V-ip2Ltg'
    response = requests.get(request_str)
    pprint(response.json())
    return HttpResponse(response)
    '''
    return render(request, 'directions.html', {})