import json
import urllib
from dataclasses import dataclass

from AppService import AppService

@dataclass
class WeatherDataService:
    longitude: float
    latitude: float
    calender_week: int


if __name__ == "__main__":
    url = "https://api.open-meteo.com/v1/forecast"

    app_service = AppService(url)
    weather_data = app_service.obtain_weather_data()

 
