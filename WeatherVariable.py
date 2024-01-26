from dataclasses import dataclass


@dataclass
class WeatherVariable:
    name: str
    description: str
    hourly: bool
    max_value: float
    min_value: float


    #def
