from django.shortcuts import render
from .models import Crime
import json


# Create your views here.

def get_crimes(request):
    #return Event.objects.filter(date_end_registration__gte=timezone.now())
    return json.dumps({"latitude": 37.777489, "longitude": -122.418202, "value": 3})