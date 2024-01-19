from dataclasses import dataclass

from AppService import AppService


@dataclass
class WeatherData:
    longitude: float
    latitude: float
    calender_week: int



if __name__ == "__main__":
    longitude = 9.9534
    latitude = 49.7913
    calendar_week = 4
    url = "https://api.open-meteo.com/v1/forecast"

    app_service = AppService()

    input_service, output_service, calendar_week_service, weather_api_service = app_service.initialize_services(url)

    # retrieve longitude & latitude from user
    #longitude, latitude = input_service.retrieve_longitude_latitude()

    # retrieve calendar week from user
    calendar_week = input_service.retrieve_calendar_week()
    start_date, end_date = calendar_week_service.compute_start_end_day(calendar_week)

    # retrieve daily weather variable (specifies the desired data)
    daily_weather_variable = input_service.retrieve_daily_weather_variable()

    daily_weather_data = weather_api_service.get_daily_data(latitude, longitude, start_date, end_date, daily_weather_variable)

    output_service.print_daily_weather_variable(daily_weather_data, daily_weather_variable)

