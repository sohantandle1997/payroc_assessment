from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(8), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    precipitation = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
