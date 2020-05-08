from django.urls import path
from . import views              # . means current directory

# define all server urls here and connect to the main urls.py
urlpatterns = [
   path("",views.index,name = 'index')    ,     # path is module where assign the routes of each page with some methods
   path('<int:flight_id>',views.flight)
]
