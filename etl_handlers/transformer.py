import xml.etree.ElementTree as ET
from metadata import Metadata


class WeatherDataTransformer:
    def transform(self, data):
        raise NotImplementedError


class JsonWeatherDataTransformer(WeatherDataTransformer):
    def transform(self, data):
        hourly_data = data[Metadata.OpenMeteoMetadata.HOURLY]
        longitude = "{:.2f}".format(data[Metadata.OpenMeteoMetadata.LONGITUDE])
        latitude = "{:.2f}".format(data[Metadata.OpenMeteoMetadata.LATITUDE])
        time_list = hourly_data[Metadata.OpenMeteoMetadata.TIME]
        temperature_list = hourly_data[Metadata.OpenMeteoMetadata.TEMPERATURE]
        precipitation_list = hourly_data[Metadata.OpenMeteoMetadata.PRECIPITATION]
        wind_speed_list = hourly_data[Metadata.OpenMeteoMetadata.WIND_SPEED]

        transformed_data = {}

        for i in range(len(time_list)):
            timestamp = time_list[i]
            temperature = temperature_list[i]
            precipitation = precipitation_list[i]
            wind_speed = wind_speed_list[i]

            date, time = timestamp.split("T")
            transformed_data[date + ' ' + time] = {
                Metadata.Constant.LONGITUDE: longitude,
                Metadata.Constant.LATITUDE: latitude,
                Metadata.Constant.DATE: date,
                Metadata.Constant.TIME: time,
                Metadata.Constant.TEMPERATURE: temperature,
                Metadata.Constant.PRECIPITATION: precipitation,
                Metadata.Constant.WIND_SPEED: wind_speed
            }

        print(transformed_data)
        return transformed_data


class XmlWeatherDataTransformer(WeatherDataTransformer):
    def transform(self, data):
        xml_root = ET.fromstring(data)

        # Location data
        longitude = "{:.2f}".format(float(
            xml_root.find(f'./{Metadata.WeatherAPIMetadata.LOCATION}/{Metadata.WeatherAPIMetadata.LONGITUDE}').text))
        latitude = "{:.2f}".format(float(
            xml_root.find(f'./{Metadata.WeatherAPIMetadata.LOCATION}/{Metadata.WeatherAPIMetadata.LATITUDE}').text))

        # Forecast data
        forecastday = xml_root.find(f'./{Metadata.WeatherAPIMetadata.FORECAST}/{Metadata.WeatherAPIMetadata.FORECAST_DAY}')

        transformed_data = {}

        for hour in forecastday.findall(f'./{Metadata.WeatherAPIMetadata.HOUR}'):
            timestamp = hour.find(f'./{Metadata.WeatherAPIMetadata.TIME}').text
            temperature = float(hour.find(f'./{Metadata.WeatherAPIMetadata.TEMPERATURE}').text)
            precipitation = float(hour.find(f'./{Metadata.WeatherAPIMetadata.PRECIPITATION}').text)
            wind_speed = float(hour.find(f'./{Metadata.WeatherAPIMetadata.WIND_SPEED}').text)

            date, time = timestamp.split()
            transformed_data[timestamp] = {
                Metadata.Constant.LONGITUDE: longitude,
                Metadata.Constant.LATITUDE: latitude,
                Metadata.Constant.DATE: date,
                Metadata.Constant.TIME: time,
                Metadata.Constant.TEMPERATURE: temperature,
                Metadata.Constant.PRECIPITATION: precipitation,
                Metadata.Constant.WIND_SPEED: wind_speed
            }

        print('xml response')
        print(transformed_data)
        return transformed_data
