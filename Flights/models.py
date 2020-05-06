from django.db import models

# Create your models here.

# class Airports(models.Model):
#     code = models.CharField(max_length=5)
#     city = models.CharField(max_length=64)
#
#     def __str__(self):
#         return f"code: {self.code} and city: {self.city}"

class Flights(models.Model):
    origin = models.CharField(max_length=64)
    # models.CASCADE for maintain the refferential Integrity
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    # whenevr call to fetching the data or String Representation
    def __str__(self):
        return f"origin: {self.origin} to destination: {self.destination} takes {self.duration}"
