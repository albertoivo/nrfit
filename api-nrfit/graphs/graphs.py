import matplotlib.pyplot as plt
from flask import Blueprint

import crud
import util

graphs = Blueprint('graphs', __name__, url_prefix='/graph')


@graphs.route('/avg_kcal_by_days/<days>')
def avg_kcal_by_days(days):
    df = crud.avg_kcal_by_days()
    column_name = 'Média dos últimos {} dias'.format(days)
    df[column_name] = round(df['kcal'].rolling(window=int(days)).mean(), 2)
    df[['kcal', column_name]].plot(figsize=(17, 6))

    return util.matplotlib_to_base64(plt)


@graphs.route('/avg_kcal_by_trained_days/<days>')
def avg_kcal_by_trained_days(days):
    df = crud.avg_kcal_by_trained_days()
    column_name = 'Média dos últimos {} dias de treino'.format(days)
    df[column_name] = round(df['kcal'].rolling(window=int(days)).mean(), 2)
    df[['kcal', column_name]].plot(figsize=(17, 6))

    return util.matplotlib_to_base64(plt)


@graphs.route('/avg_running_km_by_days/<days>')
def avg_running_km_by_days(days):
    df = crud.avg_running_km_by_days()
    column_name = 'Média de KMs corridos nos últimos {} dias'.format(days)
    df[column_name] = round(df['distance'].rolling(window=int(days)).mean(), 2)
    df[['distance', column_name]].plot(figsize=(17, 6))

    return util.matplotlib_to_base64(plt)
