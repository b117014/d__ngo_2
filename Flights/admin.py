from django.contrib import admin
from .models import Airports,Flights,Passengers
# Register your models here.

admin.site.register(Airports)             # admin access the data by using this method
admin.site.register(Flights)
admin.site.register(Passengers)
