import requests
from decouple import config

API_KEY = config("OPENWEATHER_API_KEY")


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=5
        )

        data = response.json()

        if response.status_code == 404:
            return {
                "error": "Город не найден"
            }

        return data

    except requests.exceptions.RequestException:
        return {
            "error": "API недоступен"
        }