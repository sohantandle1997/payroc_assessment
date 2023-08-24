from flask import Blueprint, make_response, jsonify, request
from etl_handlers.etl_handler import ETLHandler
from http import HTTPStatus

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/extract-transform-load', methods=['GET'])
def extract_transform_load_api():
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    forecast_days = request.args.get('forecast-days')

    _etl_handler = ETLHandler(latitude, longitude, forecast_days)
    _etl_handler.perform_etl()

    return make_response(jsonify({'message': 'ETL Successful'}), HTTPStatus.OK)