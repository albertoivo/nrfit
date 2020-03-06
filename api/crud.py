import sqlite3

import pandas as pd


def all():
    try:
        conn = sqlite3.connect('datafitness.db')
        df = pd.read_sql('select * from data_fitness order by date, sport', conn, index_col='id')
    finally:
        conn.close()

    return df.to_json(orient='records')


def by_sport(sport):
    try:
        conn = sqlite3.connect('datafitness.db')
        if sport:
            sql = 'select * from data_fitness where sport = ? order by date, sport'
        else:
            sql = 'select * from data_fitness order by date, sport'
        df = pd.read_sql(sql, conn, params={sport}, index_col='id')
    finally:
        conn.close()

    return df.to_json(orient='records')


def mean_kcal(days=7):
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select * from data_fitness order by date, sport'
        df = pd.read_sql(sql, conn, index_col='id')
        column_name = 'Média dos últimos {} dias'.format(days)
        df[column_name] = round(df['kcal'].rolling(window=int(days)).mean(), 2)
    finally:
        conn.close()

    return df.to_json(orient='records')


def mean_kcal_by_sport(sport, days):
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select * from data_fitness where sport = ? order by date, sport'
        df = pd.read_sql(sql, conn, params={sport}, index_col='id')
        column_name = 'Média dos últimos {} dias em {}'.format(days, sport)
        df[column_name] = round(df['kcal'].rolling(window=int(days)).mean(), 2)
    finally:
        conn.close()

    return df.to_json(orient='records')


def mean_kcal_by_days():
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select kcal, date from data_fitness order by date, sport'
        return pd.read_sql(sql, conn, index_col='date')
    finally:
        conn.close()


def mean_running_km_by_days(days):
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select distance, date from data_fitness where sport=\'running\' order by date'
        return pd.read_sql(sql, conn, index_col='date')
    finally:
        conn.close()
