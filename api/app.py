#!/usr/bin/env python

import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from config import Config
from models import DataFitness
from util import get_date, get_time

app = Flask(__name__)
app.config.from_object(Config)
SQLAlchemy(app)


@app.route('/add', methods=['POST'])
def add_fit_data():
    """
        {
            "date": "2019-02-02",
            "sport": "run",
            "kcal": "600",
            "duration": "1:12",
            "pace": "5:27",
            "heartrate": "143"
        }
    """
    data = request.json

    date = get_date(data)
    sport = data['sport']
    kcal = data['kcal']
    duration = get_time(data['duration'])
    distance = float(data['distance'])
    hr = data['avg_heartrate']

    fit = DataFitness(date=date, sport=sport, kcal=kcal, distance=distance,
                      duration=duration, avg_heartrate=hr)

    fit.create()

    return jsonify({
        'sucess': True
    })


# -------------------------------------------------------------------------- #
# Error handlers.
# -------------------------------------------------------------------------- #

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'code': '404',
        'description': str(e)
    }), 404


@app.errorhandler(403)
def forbidden(e):
    return jsonify({
        'code': '403',
        'description': str(e)
    }), 403


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        'code': '500',
        'description': str(e)
    }), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
