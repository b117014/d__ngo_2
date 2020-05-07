from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Flights
# Create your views here.

def index(request):
    context = {
      "flight": Flights.objects.all()
    }                                 # pass the request argument in main function
    # context is fixed name dictonary where we can pass to the html page
    return render(request,"flight/index.html",context)
