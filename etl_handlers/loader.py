from models import WeatherData
from metadata import Metadata


class Loader:
    def __init__(self, data_to_load):
        self.data_to_load = data_to_load

    def load(self):
        from app import weather_model
        for timestamp, data in self.data_to_load.items():
            latitude = data[Metadata.Constant.LATITUDE]
            longitude = data[Metadata.Constant.LONGITUDE]
            date = data[Metadata.Constant.DATE]
            time = data[Metadata.Constant.TIME]
            temperature = data[Metadata.Constant.TEMPERATURE]
            precipitation = data[Metadata.Constant.PRECIPITATION]
            wind_speed = data[Metadata.Constant.WIND_SPEED]

            weather_entry = WeatherData(
                latitude=latitude,
                longitude=longitude,
                date=date,
                time=time,
                temperature=temperature,
                precipitation=precipitation,
                wind_speed=wind_speed
            )

            weather_model.session.add(weather_entry)

        weather_model.session.commit()
