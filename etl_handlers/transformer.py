import xml.etree.ElementTree as ET


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
        precipitation_list = hourly_data["precipitation"]
        wind_speed_list = hourly_data["windspeed_10m"]

        transformed_data = {}

        for i in range(len(time_list)):
            timestamp = time_list[i]
            temperature = temperature_list[i]
            precipitation = precipitation_list[i]
            wind_speed = wind_speed_list[i]

            date, time = timestamp.split("T")
            transformed_data[date + ' ' + time] = {
                "longitude": longitude,
                "latitude": latitude,
                "date": date,
                "time": time,
                "temperature": temperature,
                "precipitation": precipitation,
                "wind_speed": wind_speed
            }

        print(transformed_data)
        return transformed_data


class XmlWeatherDataTransformer(WeatherDataTransformer):
    def transform(self, data):
        xml_root = ET.fromstring(data)

        # Location data
        longitude = float(xml_root.find('./location/lon').text)
        latitude = float(xml_root.find('./location/lat').text)

        # Forecast data
        forecastday = xml_root.find('./forecast/forecastday')

        transformed_data = {}

        for hour in forecastday.findall('./hour'):
            timestamp = hour.find('./time').text
            temperature = float(hour.find('./temp_c').text)
            precipitation = float(hour.find('./precip_mm').text)
            wind_speed = float(hour.find('./wind_kph').text)

            date, time = timestamp.split()
            transformed_data[timestamp] = {
                "longitude": longitude,
                "latitude": latitude,
                "date": date,
                "time": time,
                "temperature": temperature,
                "precipitation": precipitation,
                "wind_speed": wind_speed,
            }

        print('xml response')
        print(transformed_data)
        return transformed_data
