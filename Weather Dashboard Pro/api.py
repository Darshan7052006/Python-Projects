import os

import requests
from dotenv import load_dotenv

from cache import get_cached_data, save_cached_data
from config import REQUEST_TIMEOUT_SECONDS
from logger import logger

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"


class WeatherAPIError(Exception):
    pass


def _request(endpoint, parameters, cache_key=None):
    if not API_KEY:
        raise WeatherAPIError("API key is missing. Add OPENWEATHER_API_KEY to .env.")

    if cache_key:
        cached_data = get_cached_data(cache_key)
        if cached_data:
            logger.info("Cache hit: %s", cache_key)
            return cached_data

    parameters["appid"] = API_KEY
    try:
        response = requests.get(
            f"{BASE_URL}/{endpoint}",
            params=parameters,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
    except requests.RequestException as error:
        logger.error("Network error calling %s: %s", endpoint, error)
        raise WeatherAPIError("Could not reach the weather service. Check your internet connection.") from error

    if response.status_code == 401:
        raise WeatherAPIError("API key was rejected. Check your .env file and OpenWeather account.")
    if response.status_code == 404:
        raise WeatherAPIError("City not found. Check the city name and try again.")
    if response.status_code != 200:
        logger.error("OpenWeather error %s: %s", response.status_code, response.text)
        raise WeatherAPIError("Weather service is unavailable right now. Please try again later.")

    data = response.json()
    if cache_key:
        save_cached_data(cache_key, data)
    return data


def get_current_weather(city, units="metric"):
    return _request("weather", {"q": city, "units": units}, f"current:{city.lower()}:{units}")


def get_five_day_forecast(city, units="metric"):
    return _request("forecast", {"q": city, "units": units}, f"forecast:{city.lower()}:{units}")


def get_air_quality(city):
    weather_data = _request("weather", {"q": city}, f"coordinates:{city.lower()}")
    coordinates = weather_data["coord"]
    return _request(
        "air_pollution",
        {"lat": coordinates["lat"], "lon": coordinates["lon"]},
        f"aqi:{coordinates['lat']}:{coordinates['lon']}",
    )
