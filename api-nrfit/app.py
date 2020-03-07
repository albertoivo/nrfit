import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import Config
from graphs.graphs import graphs
from jsons.jsons import jsons
from models import DataFitness
from util import get_date, get_duration, get_data

app = Flask(__name__)
app.config.from_object(Config)
SQLAlchemy(app)

app.register_blueprint(jsons)
app.register_blueprint(graphs)


@app.route('/add', methods=['POST'])
def add():
    """
        {
            "date": "2019-02-02",
            "sport": "run",
            "kcal": "600",
            "distance": 5,
            "duration": "1:12",
            "avg_heartrate": "143"
        }
    """

    date = get_date()
    sport = get_data('sport')
    kcal = int(get_data('kcal'))
    duration = get_duration()
    distance = float(get_data('distance'))
    hr = get_data('avg_heartrate')

    fit = DataFitness(date=date, sport=sport, kcal=kcal, distance=distance, duration=duration, avg_heartrate=hr)

    fit.create()

    return jsonify({
        'success': True
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
