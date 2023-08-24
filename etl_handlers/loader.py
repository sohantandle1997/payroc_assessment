from app import db
from models import WeatherData


class Loader:
    def __init__(self, data_to_load):
        self.data_to_load = data_to_load

    def load(self):
        for timestamp, data in self.data_to_load.items():
            latitude = 52.52
            longitude = 13.419998
            date = data["date"]
            time = data["time"]
            temperature = data["temperature"]
            precipitation = data["rainfall"]
            wind_speed = 0.0

            weather_entry = WeatherData(
                latitude=latitude,
                longitude=longitude,
                date=date,
                time=time,
                temperature=temperature,
                precipitation=precipitation,
                wind_speed=wind_speed
            )

            db.session.add(weather_entry)

        db.session.commit()