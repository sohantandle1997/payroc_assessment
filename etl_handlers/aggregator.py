from metadata import Metadata


class Aggregator:
    def aggregate(self, *args, **kwargs):
        """
        Base aggregator
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError


class AverageAggregator(Aggregator):
    def aggregate(self, json_transformed_data, xml_transformed_data):
        """
        Method to average the the json and xml transformed data
        :param json_transformed_data:
        :param xml_transformed_data:
        :return:
        """
        aggregated_data = {}

        for timestamp in json_transformed_data:
            if timestamp in xml_transformed_data:
                avg_temperature = (json_transformed_data[timestamp][Metadata.Constant.TEMPERATURE] +
                                   xml_transformed_data[timestamp][Metadata.Constant.TEMPERATURE]) / 2
                avg_temperature = round(avg_temperature, 2)

                avg_precipitation = (json_transformed_data[timestamp][Metadata.Constant.PRECIPITATION] +
                                     xml_transformed_data[timestamp][Metadata.Constant.PRECIPITATION]) / 2
                avg_precipitation = round(avg_precipitation, 2)

                avg_wind_speed = (json_transformed_data[timestamp][Metadata.Constant.WIND_SPEED] +
                                  xml_transformed_data[timestamp][Metadata.Constant.WIND_SPEED]) / 2
                avg_wind_speed = round(avg_wind_speed, 2)

                aggregated_data[timestamp] = {
                    Metadata.Constant.LONGITUDE: json_transformed_data[timestamp][Metadata.Constant.LONGITUDE],
                    Metadata.Constant.LATITUDE: json_transformed_data[timestamp][Metadata.Constant.LATITUDE],
                    Metadata.Constant.DATE: json_transformed_data[timestamp][Metadata.Constant.DATE],
                    Metadata.Constant.TIME: json_transformed_data[timestamp][Metadata.Constant.TIME],
                    Metadata.Constant.TEMPERATURE: avg_temperature,
                    Metadata.Constant.PRECIPITATION: avg_precipitation,
                    Metadata.Constant.WIND_SPEED: avg_wind_speed
                }

        print(aggregated_data)
        return aggregated_data
