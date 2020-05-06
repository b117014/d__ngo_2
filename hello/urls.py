from django.urls import path
from . import views              # . means current directory

# define all server urls here and connect to the main urls.py
urlpatterns = [
   path("",views.index)

]
