from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .models import Flights
# Create your views here.

def index(request):
    context = {
      "flight": Flights.objects.all()
    }                                 # pass the request argument in main function
    # context is fixed name dictonary where we can pass to the html page
    return render(request,"flight/index.html",context)

def flight(request,flight_id):
    try:
        flight = Flights.objects.get(pk = flight_id)
    except Flights.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
      "flight":flight,
      "passenger":flight.passenger.all()
    }
    return render(request,'flight/flight.html',context)

def book(request,flight_id):

    passenger_id = request.POST["passenger"]
    return passenger_id
