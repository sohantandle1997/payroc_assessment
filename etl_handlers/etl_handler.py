from etl_handlers.transformer import JsonWeatherDataTransformer, XmlWeatherDataTransformer
from etl_handlers.extracter import JsonWeatherDataSource, XmlWeatherDataSource
from etl_handlers.aggregator import AverageAggregator
from etl_handlers.loader import Loader


class ETLHandler:
    def __init__(self, latitude, longitude, forecast_days):
        """
        Initialize ETL handler
        :param latitude:
        :param longitude:
        :param forecast_days:
        """
        self.latitude = latitude
        self.longitude = longitude
        self.forecast_days = forecast_days

    def perform_etl(self):
        """
        Method to perform extract, transform, aggregate and load
        :return:
        """
        # Extract the xml data from weatherapi.com
        xml_data_source = XmlWeatherDataSource(self.latitude, self.longitude, self.forecast_days)
        xml_raw_data = xml_data_source.fetch_data()

        # Transform xml data into standard dict format
        xml_transformer = XmlWeatherDataTransformer()
        xml_transformed_data = xml_transformer.transform(xml_raw_data)

        # Extract the json data from open-meteo.com
        json_data_source = JsonWeatherDataSource(self.latitude, self.longitude, self.forecast_days)
        json_raw_data = json_data_source.fetch_data()

        # Transform json data into standard dict format
        json_transformer = JsonWeatherDataTransformer()
        json_transformed_data = json_transformer.transform(json_raw_data)

        # Aggregate the xml and json data into standard dict format
        aggregator = AverageAggregator()
        aggregated_data = aggregator.aggregate(json_transformed_data, xml_transformed_data)

        # Load the dict data into the database
        loader = Loader(aggregated_data)
        loader.load()





