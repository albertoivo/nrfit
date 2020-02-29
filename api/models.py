from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

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
    duration = db.Column(db.Time())
    pace = db.Column(db.Time())
    heart_rate = db.Column(db.Integer)

    def create(self):
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
