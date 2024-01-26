import datetime
import json

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import seaborn

from CalendarWeekService import CalendarWeekService
from InputService import InputService
from WeatherApiService import WeatherApiService


class InteractivePlotOutputService:

    def __init__(self, url):
        self.input_service = InputService()
        self.calendar_week_service = CalendarWeekService()
        self.weather_api_service = WeatherApiService(url)
        self.current_location = 'Wuerzburg'
        self.current_weather_variable = 'Temperature'
        self.p = None
        with open("config.json", "r") as jsonfile:
            data = json.load(jsonfile)
            self.weather_variables = data["weather_variables"]
            self.locations = data["locations"]



    def plot_hourly_weather_variable(self):
        start_date, end_date = self.input_service.retrieve_start_and_end_date(self.calendar_week_service)

        # Setting Up Matplotlib, using the OOP Approach
        fig, ax = plt.subplots()

        def change_location(new_location: str):
            # get the data of the location from the dictionary
            self.current_location = new_location

            hourly_data = self.weather_api_service.get_hourly_data(self.locations[new_location], start_date, end_date, self.weather_variables[self.current_weather_variable]['url_name'])
            if self.p is not None:
                self.p.set_ydata(hourly_data[:, 1])
            else:
                self.p = ax.plot(hourly_data[:, 0], hourly_data[:, 1])[0]
                plt.tick_params(axis="x", labelrotation=-15)  # rotate the labels

            plot_settings()

        def change_weather_variable(new_weather_variable):
            self.current_weather_variable = new_weather_variable
            hourly_data = self.weather_api_service.get_hourly_data(self.locations[self.current_location], start_date,
                                                                   end_date, self.weather_variables[new_weather_variable]['url_name'])

            if self.p is not None:
                self.p.set_ydata(hourly_data[:, 1])
            else:
                self.p = ax.plot(hourly_data[:, 0], hourly_data[:, 1])[0]
                plt.tick_params(axis="x", labelrotation=-15)  # rotate the labels

            plot_settings()

        def plot_settings():
            ax.set_title(self.current_weather_variable + ' in ' + self.current_location)
            ax.set_ylim(self.weather_variables[self.current_weather_variable]['min_value'],
                        self.weather_variables[self.current_weather_variable]['max_value'])
            ax.set_ylabel(self.weather_variables[self.current_weather_variable]['unit'], rotation=0)
            plt.draw()

        # the plot is created with the first location
        change_location(self.current_location)

        # buttons with different locations
        buttons_location = RadioButtons(
            ax=plt.axes([0.1, 0.1, 0.35, 0.2]),
            labels=list(self.locations.keys()),
        )

        buttons_location.on_clicked(change_location)

        # buttons for different weather variables
        buttons_variable = RadioButtons(ax=plt.axes([0.5, 0.1, 0.35, 0.2]),
            labels=list(self.weather_variables.keys()))

        buttons_variable.on_clicked(change_weather_variable)

        # adjust the plot size
        plt.subplots_adjust(left=0.1, bottom=0.40)

        plt.show()

if __name__ == "__main__":
    url = "https://api.open-meteo.com/v1/forecast"

    interactive_plot = InteractivePlotOutputService(url)
    interactive_plot.plot_hourly_weather_variable()