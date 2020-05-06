# django
- python3 manage.py runserver    # command to run the server
- here are some modules of django where we can use for development

- Inside View.py file, define all the function which render diffrent routes

1. django.urls import path
    - path is method which is present inside django.urls and used to mange the routes just like app.get() in nodejs and @app.routes() in flask.
    - path method have two argumants, first is routes (eg:"") and second is function name which is invoked during routes calling
    - We have to also connect the main urls.py with under the project urls.py by using include

2. django.urls import include
    - this is for outside the urls.py eg. path('',include('hello.urls'))
