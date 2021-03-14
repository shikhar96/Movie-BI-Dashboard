import math
import os
import requests
import time

from bs4 import BeautifulSoup as bs
import pandas as pd
import pyodbc

urls = []

# csv_filepath = os.path.join(os.path.dirname(__file__), 'chewy_output.csv')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    "Upgrade-Insecure-Requests": "1", "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"}


def take_first_four(string):
    return int(string[:4])

# def insert_to_db():
#     updates = pd.read_csv('updated_adjusted_revenue_budget.csv')
#
#     server = 'imt563-group4.database.windows.net'
#     database = 'movie_db'
#     username = 'imt563'
#     password = 'Password'
#     conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#     cursor = conn.cursor()
#
#     for index, row in updates.iterrows():
#         # print(index,row)
#         cursor.execute(
#             "UPDATE dbo.Movies SET budget=?, revenue=?, adjusted_revenue=? WHERE id=?",
#             row.budget, row.revenue, row.adjusted_revenue,row.id
#         )
#     conn.commit()
#     cursor.close()

# def insert_to_db():
#     updates = pd.read_csv('Actor.csv')
#
#     server = 'imt563-group4.database.windows.net'
#     database = 'movie_db'
#     username = 'imt563'
#     password = 'Password'
#     conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#     cursor = conn.cursor()
#
#     for index, row in updates.iterrows():
#         print(index,row)
#         cursor.execute(
#             "INSERT INTO dbo.Actor (actor_id, actor_name) VALUES(?,?)",
#             row.actor_id, row.actor_name
#         )
#     conn.commit()
#     cursor.close()

def insert_to_db():
    updates = pd.read_csv('Movie_Actor.csv')
    updates['id'] = pd.array(updates['id'],dtype='Int64')

    movies = pd.read_csv('Movies.csv')

    updates = updates[updates['id'].isin(movies['id'])]

    updates = updates.drop_duplicates()


    server = 'imt563-group4.database.windows.net'
    database = 'movie_db'
    username = 'imt563'
    password = 'Password'
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()

    for index, row in updates.iterrows():
        print(index,row)
        cursor.execute(
            "INSERT INTO dbo.Movie_Actor (id, actor_id) VALUES(?,?)",
            row.id, row.actor_id
        )
    conn.commit()
    cursor.close()




if __name__ == '__main__':
    # crawl_urls()
    # scrape_urls()
    insert_to_db()

