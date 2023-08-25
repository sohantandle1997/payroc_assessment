from flask_sqlalchemy import SQLAlchemy
from metadata import Metadata

db = SQLAlchemy()


class WeatherData(db.Model):
    """
    Weather database model
    """
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(8), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    precipitation = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    wind_direction = db.Column(db.Float, nullable=False)

    @classmethod
    def get_hourly_weather_data(cls, latitude, longitude, date):
        """
        Method to query the weather data from the database
        :param latitude:
        :param longitude:
        :param date:
        :return:
        """
        hourly_data = cls.query.filter_by(latitude=latitude, longitude=longitude, date=date).all()
        response_data = {
            Metadata.Constant.LATITUDE: latitude,
            Metadata.Constant.LONGITUDE: longitude,
            Metadata.Constant.DATE: date,
            Metadata.Constant.HOURLY_DATA: {}
        }

        for entry in hourly_data:
            timestamp = entry.time
            response_data[Metadata.Constant.HOURLY_DATA][timestamp] = {
                Metadata.Constant.TEMPERATURE: entry.temperature,
                Metadata.Constant.PRECIPITATION: entry.precipitation,
                Metadata.Constant.WIND_SPEED: entry.wind_speed,
                Metadata.Constant.WIND_DIRECTION: entry.wind_direction
            }

        return response_data
