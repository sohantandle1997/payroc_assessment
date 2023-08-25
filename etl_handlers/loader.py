from models import WeatherData
from metadata import Metadata


class Loader:
    def __init__(self, data_to_load):
        self.data_to_load = data_to_load

    def load(self):
        """
        Method to load the transformed data onto the database
        :return:
        """
        from app import weather_model
        for timestamp, data in self.data_to_load.items():
            latitude = data[Metadata.Constant.LATITUDE]
            longitude = data[Metadata.Constant.LONGITUDE]
            date = data[Metadata.Constant.DATE]
            time = data[Metadata.Constant.TIME]

            existing_entry = WeatherData.query.filter_by(
                date=date,
                time=time,
                latitude=latitude,
                longitude=longitude
            ).first()

            temperature = data[Metadata.Constant.TEMPERATURE]
            precipitation = data[Metadata.Constant.PRECIPITATION]
            wind_speed = data[Metadata.Constant.WIND_SPEED]

            if existing_entry:
                # Update new weather parameters onto the existing entry if data already exists
                existing_entry.temperature = data[Metadata.Constant.TEMPERATURE]
                existing_entry.precipitation = data[Metadata.Constant.PRECIPITATION]
                existing_entry.wind_speed = data[Metadata.Constant.WIND_SPEED]
            else:
                new_weather_entry = WeatherData(
                    latitude=latitude,
                    longitude=longitude,
                    date=date,
                    time=time,
                    temperature=temperature,
                    precipitation=precipitation,
                    wind_speed=wind_speed
                )
                weather_model.session.add(new_weather_entry)

        weather_model.session.commit()
