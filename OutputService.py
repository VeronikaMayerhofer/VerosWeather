# prints the specific data on the console
from matplotlib import pyplot as plt
import numpy as np

class OutputService:
    def __init__(self):
        pass

    def plot_hourly_weather_variable(self, hourly_weather_data: np.ndarray, hourly_weather_variable: str):

        x = hourly_weather_data[:, 1]
        y = hourly_weather_data[:, 0]
        plt.plot(y, x, color='g', linewidth=3)
        plt.tick_params(axis="x", labelrotation=-15)  # rotate the labels

        match hourly_weather_variable:
            case 'temperature_2m':
                text = 'Temperature'
                plt.ylabel('°C', rotation=0)
            case 'apparent_temperature':
                text = 'Apparent Temperature'
                plt.ylabel('°C', rotation=0)
            case 'relative_humidity':
                text = 'Relative Humidity'
            case 'precipitation probability':
                text = 'Precipitation Probability'
            case 'rain':
                text = 'Rain'
            case 'snowfall':
                text = 'Snowfall'
        plt.title(text)
        plt.show()


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
