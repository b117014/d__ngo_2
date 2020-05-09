from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .models import Flights,Passengers
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
    try:
        passenger_id = int(request.POST['passenger'])
        passenger = Passangers.objects.get(pk=passenger_id)
        flight = Flights.objects.get(pk=flight_id)
    except KeyError:             # if does not include the data of passanger of post routes
        return render(request,'flight/error.html',{"message":"no selections"})
    except Flights.DoesNotExist:
        return render(request,'flight/error.html',{"message":"Flight does not exist"})
    except Passengers.DoesNotExist:
        return render(request,'flight/error.html',{"message":"Passenger does not exist"})

    passanger.flight.add(flight);
