import json
import urllib.request
from datetime import datetime, date, timedelta
from typing import Any


class WeatherData:
    def __init__(self, longitude, latitude, calender_week):
        self.longitude = longitude
        self.latitude = latitude
        self.calender_week = calender_week

class WeatherApiService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_sunrise_data(self, latitude: float, longitude: float, start_date: date, end_date: date) -> dict[str, Any]:
        url = f"{self.base_url}?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=sunrise,sunset"
        data = urllib.request.urlopen(url).read()
        parsed = json.loads(data)
        print(parsed)
        sunrise_data = parsed["daily"]["sunrise"]
        return sunrise_data


class CalendarWeekService:
    def __init__(self):
        pass

    def compute_start_end_day(self, calendar_week: int) -> tuple[date, date]:
        start_date = date.fromisocalendar(datetime.now().year, calendar_week, 1)
        return start_date, start_date + timedelta(weeks=1)


if __name__ == "__main__":
    longitude = 9.9534
    latitude = 49.7913
    calendar_week = 4
    url = "https://api.open-meteo.com/v1/forecast"

    calendar_week_service = CalendarWeekService()
    start_date, end_date = calendar_week_service.compute_start_end_day(calendar_week)

    weather_api_service = WeatherApiService(url)
    sunrise_data = weather_api_service.get_sunrise_data(latitude, longitude, start_date, end_date)
    print(sunrise_data)

