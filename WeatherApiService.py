import json
import urllib.request
from datetime import datetime, date, timedelta
import numpy as np

# fetches data from weather api

class WeatherApiService:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_daily_data(self, latitude: float, longitude: float, start_date: date, end_date: date, daily_weather_variable: str) -> list[datetime]:
        url = (f"{self.base_url}?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}"
               f"&daily={daily_weather_variable}")
        fetched_data = urllib.request.urlopen(url).read()
        parsed = json.loads(fetched_data)
        daily_data = parsed["daily"][daily_weather_variable]
        #print(daily_data)
        match daily_weather_variable:
            case "sunrise" | "sunset":
                data_parsed = list(map(lambda data: datetime.strptime(data, '%Y-%m-%dT%H:%M'), daily_data))
                final_daily_data = list([x.date(), x.time()] for x in data_parsed)
            case "daylight_duration" | "sunshine_duration":
                date_list = [start_date + timedelta(days=x) for x in range(7)]
                final_daily_data = list([date_list[i], np.round(daily_data[i]/60/60, 2)] for i in range(len(date_list)))
            case "temperature_2m_max" | "temperature_2m_min":
                date_list = [start_date + timedelta(days=x) for x in range(7)]
                final_daily_data = list([date_list[i], np.round(daily_data[i], 2)] for i in range(len(date_list)))

        return final_daily_data



