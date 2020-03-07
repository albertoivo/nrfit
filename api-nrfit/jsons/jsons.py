from flask import Blueprint

import crud

jsons = Blueprint('jsons', __name__, url_prefix='/json')


@jsons.route('/')
def get_all():
    df = crud.all()
    return df.to_json(orient='records')


@jsons.route('/sport/<sport>')
def by_sport(sport=""):
    df = crud.by_sport(sport)
    return df.to_json(orient='records')


@jsons.route('/avg_kcal/<days>')
def avg_kcal(days):
    df = crud.avg_kcal()
    column_name = 'Média dos últimos {} dias'.format(days)
    df[column_name] = round(df['kcal'].rolling(window=int(days)).mean(), 2)

    return df.to_json(orient='records')


@jsons.route('/avg_kcal_by_sport/<sport>/<days>')
def avg_kcal_by_sport(sport, days):
    df = crud.avg_kcal_by_sport(sport, days)
    column_name = 'Média dos últimos {} dias em {}'.format(days, sport)
    df[column_name] = round(df['kcal'].rolling(window=int(days)).mean(), 2)

    return df.to_json(orient='records')
