import xml.etree.ElementTree as ET
from metadata import Metadata


class WeatherDataTransformer:
    def transform(self, data):
        """
        Base transform method
        :param data:
        :return:
        """
        raise NotImplementedError


class JsonWeatherDataTransformer(WeatherDataTransformer):
    def transform(self, data):
        """
        Method to transform XML weather forecast data from open-meteo.com
        :param data:
        :return:
        """
        hourly_data = data[Metadata.OpenMeteoMetadata.HOURLY]
        longitude = "{:.2f}".format(data[Metadata.OpenMeteoMetadata.LONGITUDE])
        latitude = "{:.2f}".format(data[Metadata.OpenMeteoMetadata.LATITUDE])
        time_list = hourly_data[Metadata.OpenMeteoMetadata.TIME]
        temperature_list = hourly_data[Metadata.OpenMeteoMetadata.TEMPERATURE]
        precipitation_list = hourly_data[Metadata.OpenMeteoMetadata.PRECIPITATION]
        wind_speed_list = hourly_data[Metadata.OpenMeteoMetadata.WIND_SPEED]
        wind_direction_list = hourly_data[Metadata.OpenMeteoMetadata.WIND_SPEED]

        transformed_data = {}

        for i in range(len(time_list)):
            timestamp = time_list[i]
            temperature = temperature_list[i]
            precipitation = precipitation_list[i]
            wind_speed = wind_speed_list[i]
            wind_direction = wind_direction_list[i]

            date, time = timestamp.split("T")
            transformed_data[date + ' ' + time] = {
                Metadata.Constant.LONGITUDE: longitude,
                Metadata.Constant.LATITUDE: latitude,
                Metadata.Constant.DATE: date,
                Metadata.Constant.TIME: time,
                Metadata.Constant.TEMPERATURE: temperature,
                Metadata.Constant.PRECIPITATION: precipitation,
                Metadata.Constant.WIND_SPEED: wind_speed,
                Metadata.Constant.WIND_DIRECTION: wind_direction
            }

        return transformed_data


class XmlWeatherDataTransformer(WeatherDataTransformer):
    def transform(self, data):
        """
        Method to transform XML weather forecast data from weatherapi.com
        :param data:
        :return:
        """
        xml_root = ET.fromstring(data)

        # Location data
        longitude = "{:.2f}".format(float(
            xml_root.find(f'./{Metadata.WeatherAPIMetadata.LOCATION}/{Metadata.WeatherAPIMetadata.LONGITUDE}').text))
        latitude = "{:.2f}".format(float(
            xml_root.find(f'./{Metadata.WeatherAPIMetadata.LOCATION}/{Metadata.WeatherAPIMetadata.LATITUDE}').text))

        # Forecast data
        forecast = xml_root.find(f'./{Metadata.WeatherAPIMetadata.FORECAST}')
        forecast_days = xml_root.find(f'./{Metadata.WeatherAPIMetadata.FORECAST}/{Metadata.WeatherAPIMetadata.FORECAST_DAY}')

        transformed_data = {}

        loop_count = 0

        for forecast_day in forecast.findall(f'./{Metadata.WeatherAPIMetadata.FORECAST_DAY}'):
            for hour in forecast_day.findall(f'./{Metadata.WeatherAPIMetadata.HOUR}'):
                loop_count += 1
                timestamp = hour.find(f'./{Metadata.WeatherAPIMetadata.TIME}').text
                temperature = float(hour.find(f'./{Metadata.WeatherAPIMetadata.TEMPERATURE}').text)
                precipitation = float(hour.find(f'./{Metadata.WeatherAPIMetadata.PRECIPITATION}').text)
                wind_speed = float(hour.find(f'./{Metadata.WeatherAPIMetadata.WIND_SPEED}').text)
                wind_direction = float(hour.find(f'./{Metadata.WeatherAPIMetadata.WIND_DIRECTION}').text)

                date, time = timestamp.split()
                transformed_data[timestamp] = {
                    Metadata.Constant.LONGITUDE: longitude,
                    Metadata.Constant.LATITUDE: latitude,
                    Metadata.Constant.DATE: date,
                    Metadata.Constant.TIME: time,
                    Metadata.Constant.TEMPERATURE: temperature,
                    Metadata.Constant.PRECIPITATION: precipitation,
                    Metadata.Constant.WIND_SPEED: wind_speed,
                    Metadata.Constant.WIND_DIRECTION: wind_direction
                }

        return transformed_data
