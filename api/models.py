from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from datetime import timedelta
from util import get_time

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class DataFitness(db.Model):
    __tablename__ = 'data_fitness'

    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    kcal = db.Column(db.Integer)
    distance = db.Column(db.Float)
    duration = db.Column(db.Time())
    pace = db.Column(db.Float)
    avg_speed = db.Column(db.Float)
    avg_heartrate = db.Column(db.Float)

    def create(self):
        self.avg_speed = round((self.distance / (timedelta(hours=self.duration.hour, minutes=self.duration.minute).total_seconds() / 3600)), 2)
        self.pace = round(((timedelta(hours=self.duration.hour, minutes=self.duration.minute).total_seconds() / 60) / self.distance), 2)

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'sport': self.sport,
            'date': self.date,
            'kcal': self.kcal,
            'duration': self.duration,
            'pace': self.pace,
            'heart_rate': self.heart_rate
        }
