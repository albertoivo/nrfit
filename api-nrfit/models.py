import datetime
from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class DataFitness(db.Model):
    __tablename__ = 'data_fitness'

    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.String(30), nullable=False)
    date = db.Column(db.Date(), nullable=False, default=datetime.datetime.now().date())
    kcal = db.Column(db.Integer)
    distance = db.Column(db.Float)
    duration = db.Column(db.Time())
    avg_heartrate = db.Column(db.Float)
    pace = db.Column(db.Float)
    avg_speed = db.Column(db.Float)

    def create(self):
        hour = self.duration.hour
        minute = self.duration.minute

        self.avg_speed = round((self.distance / (timedelta(hours=hour, minutes=minute).total_seconds() / 3600)), 2)
        self.pace = round(((timedelta(hours=hour, minutes=minute).total_seconds() / 60) / self.distance), 2)

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'sport': self.sport,
            'kcal': self.kcal,
            'duration': self.duration,
            'distance': self.distance,
            'pace': self.pace,
            'avg_speed': self.avg_speed,
            'avg_heartrate': self.avg_heartrate
        }
