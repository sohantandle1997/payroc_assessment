import requests
from metadata import Metadata


class WeatherDataSource:
    def __init__(self, latitude, longitude, forecast_days):
        """
        Base init for weather data extractor
        :param latitude:
        :param longitude:
        :param forecast_days:
        """
        self.latitude = latitude
        self.longitude = longitude
        self.forecast_days = forecast_days

    def fetch_data(self):
        """
        Base method to fetch data
        :return:
        """
        raise NotImplementedError


class JsonWeatherDataSource(WeatherDataSource):
    def __init__(self, latitude, longitude, forecast_days):
        """
        Initialize json weather data extractor
        :param latitude:
        :param longitude:
        :param forecast_days:
        """
        super().__init__(latitude, longitude, forecast_days)

    def fetch_data(self):
        """
        Method to extract data from open-meteo.com
        :return:
        """
        _url = Metadata.OpenMeteoMetadata.URL.format(self.latitude, self.longitude, self.forecast_days)
        _response = requests.get(_url)
        return _response.json()


class XmlWeatherDataSource(WeatherDataSource):
    def __init__(self, latitude, longitude, forecast_days):
        """
        Initialize xml weather data extractor
        :param latitude:
        :param longitude:
        :param forecast_days:
        """
        super().__init__(latitude, longitude, forecast_days)

    def fetch_data(self):
        """
        Method to extract data from weatherapi.com
        :return:
        """
        _url = Metadata.WeatherAPIMetadata.URL.format(self.latitude, self.longitude, self.forecast_days)
        _response = requests.get(_url)
        xml_content = _response.content
        return xml_content
