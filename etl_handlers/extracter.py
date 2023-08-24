import requests
from metadata import Metadata


class WeatherDataSource:
    def __init__(self, latitude, longitude, forecast_days):
        self.latitude = latitude
        self.longitude = longitude
        self.forecast_days = forecast_days

    def fetch_data(self):
        raise NotImplementedError


class JsonWeatherDataSource(WeatherDataSource):
    def __init__(self, latitude, longitude, forecast_days):
        super().__init__(latitude, longitude, forecast_days)

    def fetch_data(self):
        _url = Metadata.OpenMeteoMetadata.URL.format(self.latitude, self.longitude, self.forecast_days)
        _response = requests.get(_url)
        return _response.json()


class XmlWeatherDataSource(WeatherDataSource):
    def __init__(self, latitude, longitude, forecast_days):
        super().__init__(latitude, longitude, forecast_days)

    def fetch_data(self):
        _url = Metadata.WeatherAPIMetadata.URL.format(self.latitude, self.longitude, self.forecast_days)
        _response = requests.get(_url)
        xml_content = _response.content
        # xml_root = ET.fromstring(xml_content)
        # print(xml_root)
        return xml_content