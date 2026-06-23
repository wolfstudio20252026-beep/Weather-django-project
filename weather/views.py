# views.py
from django.shortcuts import render, redirect

from .forms import CitySearchForm
from .services import get_weather


def weather_view(request):
    form = CitySearchForm()

    if request.method == "POST":
        form = CitySearchForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data["city"]

            return redirect("weather_result", city=city)

    return render(request, "weather/index.html", {"form": form})


def weather_result(request, city):
    data = get_weather(city)

    if "error" in data:
        return render(
            request,
            "weather/result.html",
            {"error": data["error"]}
        )

    weather = {
        "city": city,
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    }

    return render(
        request,
        "weather/result.html",
        {"weather": weather}
    )