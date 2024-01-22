import WeatherApiService

class OutputService:
    def __init__(self):
        pass

    def print_daily_weather_variable(self, daily_weather_data, daily_weather_variable: str):
        match daily_weather_variable:
            case 'sunrise':
                self.print_sunrise_data(daily_weather_data)
            case 'sunset':
                self.print_sunset_data(daily_weather_data)
            case 'daylight_duration':
                self.print_daylight_duration_data(daily_weather_data)
            case 'sunshine_duration':
                self.print_sunshine_duration_data(daily_weather_data)
            case 'temperature_2m_min':
                self.print_min_temperature_data(daily_weather_data)
            case 'temperature_2m_max':
                self.print_max_temperature_data(daily_weather_data)

    def print_sunrise_data(self, sunrise_data):
        for data in sunrise_data:
            print(f"On {data[0]}, the sun rises at {data[1]}.")

    def print_sunset_data(self, sunset_data):
        for data in sunset_data:
            print(f"On {data[0]}, the suns sets at {data[1]}.")

    def print_daylight_duration_data(self, daylight_data):
        for data in daylight_data:
            print(f"On {data[0]}, the daylight duration is {data[1]} hours.")

    def print_sunshine_duration_data(self, sunshine_data):
        for data in sunshine_data:
            print(f"On {data[0]}, the sunshine duration is {data[1]} hours.")

    def print_min_temperature_data(self, min_temperature_data):
        for data in min_temperature_data:
            print(f"On {data[0]}, the minimum temperature is {data[1]} degrees Celsius.")

    def print_max_temperature_data(self, max_temperature_data):
        for data in max_temperature_data:
            print(f"On {data[0]}, the max temperature is {data[1]} degrees Celsius.")
