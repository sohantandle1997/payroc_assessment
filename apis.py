from flask import Blueprint, make_response, jsonify, request
from etl_handlers.etl_handler import ETLHandler
from http import HTTPStatus

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/extract-transform-load', methods=['GET'])
def extract_transform_load_api():
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    forecast_days = request.args.get('forecast-days')

    if int(forecast_days) > 14:
        return make_response(jsonify({'message': 'Invalid forecast-days, max forecast upto 14 days'}), HTTPStatus.BAD_REQUEST)

    if latitude and longitude and forecast_days:
        try:
            _etl_handler = ETLHandler(latitude, longitude, forecast_days)
            _etl_handler.perform_etl()
        except:
            return make_response(jsonify({'message': 'Failed to perform ETL'}), HTTPStatus.INTERNAL_SERVER_ERROR)

        return make_response(jsonify({'message': 'ETL Successful'}), HTTPStatus.OK)

    return make_response(jsonify({'message': 'Invalid request parameters'}), HTTPStatus.BAD_REQUEST)
