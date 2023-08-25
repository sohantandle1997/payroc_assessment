class Metadata:
    class OpenMeteoMetadata:
        URL = 'https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&hourly=temperature_2m,' \
              'precipitation,windspeed_10m,winddirection_10m&forecast_days={2}'
        # Request Parameters
        LATITUDE = 'latitude'
        LONGITUDE = 'longitude'
        HOURLY = 'hourly'
        FORECAST_DAYS = 'forecast_days'

        # Response Parameters
        TIME = "time"
        TEMPERATURE = "temperature_2m"
        PRECIPITATION = "precipitation"
        WIND_SPEED = "windspeed_10m"
        WIND_DIRECTION = "winddirection_10m"

    class WeatherAPIMetadata:
        URL = 'http://api.weatherapi.com/v1/forecast.xml?key=bcfcd72be62b456285c173318232408&q={0},{1}&days={2}'

        # Request Parameters
        KEY = 'key'
        Q = 'q'
        days = 'days'

        # Response Parameters
        LOCATION = "location"
        LONGITUDE = "lon"
        LATITUDE = "lat"
        FORECAST_DAY = "forecastday"
        FORECAST = "forecast"
        TIME = "time"
        HOUR = "hour"
        TEMPERATURE = "temp_c"
        PRECIPITATION = "precip_mm"
        WIND_SPEED = "wind_kph"
        WIND_DIRECTION = "wind_degree"

    class Constant:
        LONGITUDE = "longitude"
        LATITUDE = "latitude"
        DATE = "date"
        TIME = "time"
        TEMPERATURE = "temperature"
        PRECIPITATION = "precipitation"
        WIND_SPEED = "wind_speed"
        WIND_DIRECTION = "wind_direction"
        HOURLY_DATA = "hourly_data"

