from django.urls import path
from django.shortcuts import render
from . import views
urlpatterns = [
    path("", views.weather_view, name="weather"),
    path("weather/<str:city>/", views.weather_result, name="weather_result"),
    path("login/", lambda request: render(request, "weather/login.html"), name="login"),
    path("register/", lambda request: render(request, "weather/register.html"), name="register"),
]