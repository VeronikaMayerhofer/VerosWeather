import datetime

from CalendarWeekService import CalendarWeekService

# fetches user input from console

class InputService:
    def __init__(self):
        pass

    def retrieve_input_data_from_user(self, calendar_week_service: CalendarWeekService) -> tuple[datetime.date, datetime.date, datetime,]:
        # default values
        # coordinates for Wuerzburg, Germany
        longitude = 9.9
        latitude = 49.8

        calendar_week = 4

        # retrieve longitude & latitude from user
        #longitude, latitude = self.retrieve_longitude_latitude()
        location = [latitude, longitude]
        # retrieve start and end date from user
        start_date, end_date = self.retrieve_start_and_end_date(calendar_week_service)

        # retrieve daily weather variable (specifies the desired data)
        daily_weather_variable = self.retrieve_daily_weather_variable()

        # retrieve hourly weather variable
        hourly_weather_variable = self.retrieve_hourly_weather_variable()

        return start_date, end_date, daily_weather_variable, hourly_weather_variable, location

    def retrieve_daily_weather_variable(self):
        print("Inset the desired daily weather variable. You can choose between the following: \n 1: sunrise \n "
              "2: sunset \n 3: daylight duration \n 4: sunshine duration \n 5: maximum temperature \n "
              "6: minimum temperature.")
        weather_input = input()
        daily_weather_variable = self.retrieve_daily_weather_variable_from_input(weather_input)
        return daily_weather_variable

    def retrieve_daily_weather_variable_from_input(self, input: str) -> str:
        match input:
            case '1' | "sunrise":
                daily_weather_variable = 'sunrise'
            case '2' | "sunset":
                daily_weather_variable = 'sunset'
            case '3' | "daylight duration":
                daily_weather_variable = 'daylight_duration'
            case '4' | "sunshine duration":
                daily_weather_variable = 'sunshine_duration'
            case '5' | "maximum temperature":
                daily_weather_variable = 'temperature_2m_max'
            case '6' | "minimum temperature":
                daily_weather_variable = 'temperature_2m_min'
            case _:
                raise Exception("Invalid input.")
        return daily_weather_variable

    def retrieve_hourly_weather_variable(self):
        print("Inset the desired hourly weather variable. You can choose between the following: \n 1: temperature \n "
              "2: apparent temperature \n 3: relative humidity \n 4: precipitation probability \n 5: rain \n "
              "6: snowfall.")
        weather_input = input()
        hourly_weather_variable = self.retrieve_hourly_weather_variable_from_input(weather_input)
        return hourly_weather_variable

    def retrieve_hourly_weather_variable_from_input(self, input: str) -> str:
        match input:
            case '1' | "temperature":
                hourly_weather_variable = 'temperature_2m'
            case '2' | "apparent temperature":
                hourly_weather_variable = 'apparent_temperature'
            case '3' | "relative humidity":
                hourly_weather_variable = 'relative_humidity_2m'
            case '4' | "precipitation probability":
                hourly_weather_variable = 'precipitation_probability'
            case '5' | "rain":
                hourly_weather_variable = 'rain'
            case '6' | "snowfall":
                hourly_weather_variable = 'snowfall'
            case _:
                raise Exception("Invalid input.")
        return hourly_weather_variable

    def retrieve_longitude_latitude(self):
        print("Insert longitude and latitude:")
        input_longitude_latitude = input().split(", ")
        longitude = float(input_longitude_latitude[0])
        latitude = float(input_longitude_latitude[1])
        return longitude, latitude

    def retrieve_start_and_end_date(self, calendar_week_service: CalendarWeekService) -> tuple[datetime.date, datetime]:
        print("Insert start and end date of the weather data (YYYY-MM-DD, YYYY-MM-DD) or the desired calender week:")
        input_time = input()
        try:
            start_date, end_date = input_time.split(", ")
            res_1 = bool(datetime.datetime.strptime(start_date, '%Y-%m-%d'))
            res_2 = bool(datetime.datetime.strptime(end_date, '%Y-%m-%d'))
            if res_1 != res_2:
                raise Exception("Invalid start and end date.")
            else: res = True
        except ValueError:
            res = False
        if res == True:
            start_date, end_date = input_time.split(", ")
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        else:
            start_date, end_date = calendar_week_service.compute_start_end_day(int(input_time))
        return start_date, end_date

    def retrieve_calendar_week(self):
        print("Insert calendar week:")
        calendar_week = int(input())
        return calendar_week

    def retrieve_only_start_end_date(self):
        print("Insert start and end date of the weather data (YYYY-MM-DD, YYYY-MM-DD):.")
        start_date, end_date = input().split(", ")
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')
        return start_date, end_date


