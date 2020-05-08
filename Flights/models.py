from django.db import models

# Create your models here.

class Airports(models.Model):
    code = models.CharField(max_length=4)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f" {self.city}"

class Flights(models.Model):
    origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="departure")
    # models.CASCADE for maintain the refferential Integrity
    # related name are used to to access the data from base class
    destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="arrival")

    duration = models.IntegerField()

    # whenevr call to fetching the data or String Representation
    def __str__(self):
        return f" {self.origin} to {self.destination} takes {self.duration}"

class Passengers(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flights, blank = True, related_name="passenger")

    def __str__(self):
        return f"{self.first} {self.last}"
