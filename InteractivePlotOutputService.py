import datetime

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import seaborn

from CalendarWeekService import CalendarWeekService
from InputService import InputService
from WeatherApiService import WeatherApiService

seaborn.set_style("darkgrid")


class InteractivePlotOutputService:

    def __init__(self, url):
        self.locations = {
            'Würzburg': ['49.8', '10.0'],
            'Oslo': ['59.9', '10.8'],
            'Heilsbronn': ['49.3', '10.8'],
            'Halsbach, Lohr am Main': ['50.0', '9.7'],
            'Ho-Chi-Minh City': ['10.8', '106.7'],
        }
        self.input_service = InputService()
        self.calendar_week_service = CalendarWeekService()
        self.weather_api_service = WeatherApiService(url)
        self.p = None

    def plot_hourly_weather_variable(self, hourly_weather_variable: str):
        start_date, end_date = self.input_service.retrieve_start_and_end_date(self.calendar_week_service)

        # Setting Up Matplotlib, using the OOP Approach
        fig, ax = plt.subplots()
        # the plot is created with the first location

        def change_location(new_location: str):
            # get the data of the location from the dictionary
            hourly_data = self.weather_api_service.get_hourly_data(self.locations[new_location], start_date, end_date, hourly_weather_variable)
            if self.p is not None:
                self.p.set_ydata(hourly_data[:, 1])
                plt.draw()
            else:
                self.p = ax.plot(hourly_data[:, 0], hourly_data[:, 1])[0]
                yRange = list(range(-20, 40, 5))
                ax.set_yticks(yRange)
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

            ax.set_title(text + ' in ' + new_location)


        change_location('Würzburg')

        buttons_location = RadioButtons(
            ax=plt.axes([0.1, 0.1, 0.2, 0.2]),
            labels=list(self.locations.keys())
        )

        buttons_location.on_clicked(change_location)

        # adjust the plot size
        plt.subplots_adjust(left=0.1, bottom=0.40)

        plt.show()

if __name__ == "__main__":
    url = "https://api.open-meteo.com/v1/forecast"

    interactive_plot = InteractivePlotOutputService(url)
    interactive_plot.plot_hourly_weather_variable('temperature_2m')