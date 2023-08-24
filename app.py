from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import WeatherData, db as weather_model
from apis import api_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'  # SQLite database file
app.register_blueprint(api_blueprint)

weather_model.init_app(app)

with app.app_context():
    weather_model.create_all()


# @app.route('/extract-transform-load', methods=['POST'])
# def etl():
#     print("api called")
#     return make_response(jsonify({'msg': 'hi'}), 200)


if __name__ == '__main__':
    app.run(port=7050)
