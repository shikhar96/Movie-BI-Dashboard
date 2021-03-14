import math
import os
import requests
import time

from bs4 import BeautifulSoup as bs
import pandas as pd
import pyodbc

def insert_to_db():
    movies = pd.read_csv('Movies.csv')
    adjusted_inflation = pd.read_csv('adjust_inflation.csv')
    movies['release_year'] = movies['release_date'].apply(take_first_four)
    new = movies.merge(adjusted_inflation, left_on='release_year', right_on='year',how='left')
    new['adjusted_revenue'] = (9.37/new['cost_per_ticket'])*new['revenue']
    new['adjusted_revenue'] = new['adjusted_revenue'].fillna(0)
    new['adjusted_revenue'] = new['adjusted_revenue'].apply(lambda x: round(x, 2))

    server = 'imt563-group4.database.windows.net'
    database = 'movie_db'
    username = 'imt563'
    password = 'Password'
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()

    for index, row in new.iterrows():
        # print(index,row)
        cursor.execute(
            "INSERT INTO dbo.temp (id,adjusted_revenue) VALUES(?,?)",
            row.id, row.adjusted_revenue
        )
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    insert_to_db()

