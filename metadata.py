class Metadata:
    class OpenMeteoMetadata:
        URL = 'https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&hourly=temperature_2m,' \
              'precipitation_probability&forecast_days={2}'
        # Request Parameters
        LATITUDE = 'latitude'
        LONGITUDE = 'longitude'
        HOURLY = 'hourly'
        FORECAST_DAYS = 'forecast_days'

        # Response Parameters

    class WeatherAPIMetadata:
        URL = 'http://api.weatherapi.com/v1/forecast.xml?key=bcfcd72be62b456285c173318232408&q={0},{1}&days={2}'

        # Request Parameters
        KEY = 'key'
        Q = 'q'
        days = 'days'

        # Response Parameters
