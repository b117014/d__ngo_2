from django.contrib.auth import authenticate,login,logout
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .models import Flights,Passengers
from django.urls import reverse
# Create your views here.

def index(request):
    context = {
      "flight": Flights.objects.all()
    }                                 # pass the request argument in main function
    # context is fixed name dictonary where we can pass to the html page
    return render(request,"flight/index.html",context)


# login
def userAuth(request):

    if not request.user.is_authenticate:   #request.user.is_authenticate that is built in django and also request.user
        return HttpResponse("You have not logged in")
    constex = {
    "user":request.user
    }

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
    print("hrll")
    try:
        passenger_id = int(request.POST['passenger'])
        passenger = Passengers.objects.get(pk=passenger_id)
        flight = Flights.objects.get(pk=flight_id)
        print(passenger_id,passenger)
    except KeyError:             # if does not include the data of passanger of post routes
        return render(request,'flight/error.html',{"message":"no selections"})
    except Flights.DoesNotExist:
        return render(request,'flight/error.html',{"message":"Flight does not exist"})
    except Passengers.DoesNotExist:
        return render(request,'flight/error.html',{"message":"Passenger does not exist"})

    passenger.flight.add(flight);
    passenger.save()
    return HttpResponseRedirect(reverse('index'))     # to redirect the flight routes

def booking(request,flight_id):
    return render(request,'flight/book.html');
