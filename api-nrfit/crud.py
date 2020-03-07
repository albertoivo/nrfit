import sqlite3

import pandas as pd


def all():
    try:
        conn = sqlite3.connect('datafitness.db')
        return pd.read_sql('select * from data_fitness order by date, sport', conn, index_col='id')
    finally:
        conn.close()


def by_sport(sport):
    try:
        conn = sqlite3.connect('datafitness.db')
        if sport:
            sql = 'select * from data_fitness where sport = ? order by date, sport'
        else:
            sql = 'select * from data_fitness order by date, sport'
        return pd.read_sql(sql, conn, params={sport}, index_col='id')
    finally:
        conn.close()


def avg_kcal():
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select * from data_fitness order by date, sport'
        return pd.read_sql(sql, conn, index_col='id')
    finally:
        conn.close()


def avg_kcal_by_sport(sport, days):
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select * from data_fitness where sport = ? order by date, sport'
        return pd.read_sql(sql, conn, params={sport}, index_col='id')
    finally:
        conn.close()


def avg_kcal_by_days():
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select kcal, date from data_fitness order by date, sport'
        return pd.read_sql(sql, conn, index_col='date')
    finally:
        conn.close()


def avg_kcal_by_trained_days():
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select kcal, date from data_fitness where kcal <> 0 order by date, sport'
        return pd.read_sql(sql, conn, index_col='date')
    finally:
        conn.close()


def avg_running_km_by_days():
    try:
        conn = sqlite3.connect('datafitness.db')
        sql = 'select distance, date from data_fitness where sport=\'running\' order by date'
        return pd.read_sql(sql, conn, index_col='date')
    finally:
        conn.close()
