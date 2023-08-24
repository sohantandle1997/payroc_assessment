from metadata import Metadata
import requests
import xml.etree.ElementTree as ET


class ETLHandler:
    def __init__(self, latitude, longitude, forecast_days):
        self.latitude = latitude
        self.longitude = longitude
        self.forecast_days = forecast_days

    def perform_etl(self):
        # self.call_open_meteo_api()
        # self.call_weather_api()
        # xml_data_source = XmlWeatherDataSource(self.latitude, self.longitude, self.forecast_days)
        # xml_data_source.fetch_data()

        json_data_source = JsonWeatherDataSource(self.latitude, self.longitude, self.forecast_days)
        json_data = json_data_source.fetch_data()

        json_transformer = JsonWeatherDataTransformer()
        json_transformer.transform(json_data)

    def extract(self):
        pass

    def transform(self):
        pass

    def load(self):
        pass

    def call_open_meteo_api(self):
        _url = Metadata.OpenMeteoMetadata.URL.format(self.latitude, self.longitude, self.forecast_days)

        _response = requests.get(_url)

        print(_response.json())

    def call_weather_api(self):
        _url = Metadata.WeatherAPIMetadata.URL.format(self.latitude, self.longitude, self.forecast_days)

        _response = requests.get(_url)

        print(_response.content)


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


class WeatherDataTransformer:
    def transform(self, data):
        raise NotImplementedError


class JsonWeatherDataTransformer(WeatherDataTransformer):
    def transform(self, data):
        hourly_data = data["hourly"]
        longitude = data["longitude"]
        latitude = data["latitude"]
        time_list = hourly_data["time"]
        temperature_list = hourly_data["temperature_2m"]
        rainfall_list = hourly_data["precipitation_probability"]

        result = {}

        for i in range(len(time_list)):
            timestamp = time_list[i]
            temperature = temperature_list[i]
            rainfall = rainfall_list[i]

            date, time = timestamp.split("T")
            result[timestamp] = {
                "longitude": longitude,
                "latitude": latitude,
                "date": date,
                "time": time,
                "temperature": temperature,
                "rainfall": rainfall
            }

        print(result)
        return result


class XmlWeatherDataTransformer(WeatherDataTransformer):
    def transform(self, data):
        pass