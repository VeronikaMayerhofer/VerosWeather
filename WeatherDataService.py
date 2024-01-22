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

    input_service, output_service, calendar_week_service, weather_api_service = app_service.initialize_services(url)

    start_date, end_date, daily_weather_variable, longitude, latitude = input_service.retrieve_input_data_from_user(calendar_week_service)

    url = (f"{url}?latitude={latitude}&longitude={longitude}"
               f"&hourly=temperature_2m&start_date=2024-01-15&end_date=2024-01-16")
    fetched_data = urllib.request.urlopen(url).read()
    parsed = json.loads(fetched_data)
    daily_data = parsed["hourly"]['temperature_2m']
    print(len(daily_data))
    print(daily_data)
