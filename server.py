# uvicorn server:app --reload

import datetime

import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from WeatherApiService import WeatherApiService

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

weather_service = WeatherApiService("https://api.open-meteo.com/v1/forecast")


@app.get("/weather/{weather_variable}")
def test(latitude: float, longitude: float, weather_variable: str):
    weather_data = weather_service.get_hourly_data(np.array([latitude, longitude]), datetime.date.today(),
                                                   datetime.date.today() + datetime.timedelta(days=1), weather_variable)
    return weather_data
