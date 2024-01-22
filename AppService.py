import urllib

from InputService import InputService
from OutputService import OutputService
from WeatherApiService import WeatherApiService
from CalendarWeekService import CalendarWeekService

# connects the other services to obtain desired weather data

class AppService:
    def __init__(self,  url: str):
        self.input_service = InputService()
        self.output_service = OutputService()
        self.calendar_week_service = CalendarWeekService()
        self.weather_api_service = WeatherApiService(url)

    def obtain_weather_data(self):
        start_date, end_date, daily_weather_variable, longitude, latitude = self.input_service.retrieve_input_data_from_user(
            self.calendar_week_service)

        daily_weather_data = self.weather_api_service.get_daily_data(latitude, longitude, start_date, end_date,
                                                                daily_weather_variable)
        self.output_service.print_daily_weather_variable(daily_weather_data, daily_weather_variable)
        return daily_weather_data

    def obtain_hourly_weather_data(self):
        start_date, end_date, daily_weather_variable, longitude, latitude = self.input_service.retrieve_input_data_from_user(
            self.calendar_week_service)

        hourly_weather_data = self.weather_api_service.get_daily_data(latitude, longitude, start_date, end_date,
                                                                     daily_weather_variable)
        self.output_service.print_daily_weather_variable(hourly_weather_data, daily_weather_variable)
        return hourly_weather_data

    def initialize_services(self, url: str):
        input_service = InputService()
        output_service = OutputService()
        calendar_week_service = CalendarWeekService()
        weather_api_service = WeatherApiService(url)
        return input_service, output_service, calendar_week_service, weather_api_service