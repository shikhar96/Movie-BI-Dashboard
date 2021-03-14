import pandas as pd
import re
import os
import requests
from bs4 import BeautifulSoup as bs
import time

def clean_title(title_string):
    title_string = re.sub('[^A-Za-z0-9- ]+', '', title_string)
    title_string = title_string.lower()
    title_string = re.sub('[ ]', '_', title_string)
    title_string = re.sub('-', '_', title_string)
    return title_string

def clean_process():
    movies = pd.read_csv('Movies.csv')
    TMDB = pd.read_csv('TMDB_Denormalized.csv')
    movies['imdb_id'] = TMDB['imdb_id']
    title = movies['title']
    cleaned_title = title.apply(clean_title)
    df_cleaned_title = pd.DataFrame(cleaned_title)
    df_cleaned_title.set_index(df_cleaned_title.index)
    df_cleaned_title['website_title'] = 'None'
    return df_cleaned_title


urls = []

def crawl_urls(df_cleaned_title):
    i = 0
    for title in df_cleaned_title['title'][:5]:
        try:
            pageUrl = "https://www.rottentomatoes.com/m/{}".format(title)
            page = requests.get(pageUrl)
            if page.status_code == 404:
                print('Status code 404 issue on: ', pageUrl)
                df_cleaned_title['website_title'][i] = pageUrl
                i += 1
                continue
            # soup = bs(page.content, 'html.parser')
            df_cleaned_title['website_title'][i] = title
            print("Found: ", pageUrl)
            urls.append(pageUrl)
            i += 1
            # time.sleep(1)
        except:
            print('An error occured on: ', pageUrl)
            df_cleaned_title['website_title'][i] = pageUrl
            i += 1
    print(urls)


def scrape_urls():
    critic_scores = pd.DataFrame(columns=['title','critic_score'])
    titles = pd.read_csv('final_title_output_modified.csv')
    movies = pd.read_csv('Movies.csv')

    for title in titles['final_title']:
        # Get critic score #type int
        critic_score = 0

        if title == 'None':
            critic_score = -1
            continue

        url = 'https://www.rottentomatoes.com/m/{}'.format(title)
        page = requests.get(url)
        soup = bs(page.content, "html.parser")

        try:
            critic_score = int(soup.find('score-board')['tomatometerscore'].strip())
        except:
            critic_score = -1

        critic_scores = critic_scores.append({'title': title,'critic_score':critic_score},ignore_index = True)

    critic_scores['id'] = movies['id']

    csv_filepath = os.path.join(os.path.dirname(__file__), 'critic_score_output.csv')
    critic_scores.to_csv(csv_filepath, index=False)




def recheck_urls():

    df = pd.read_csv('website_title_error_output2.csv')
    for i in range(len(df)):
        if pd.isna(df['cleaned_website_title'][i]):
            df['cleaned_website_title'][i] = df['website_title'][i]
    i = 0
    df['final_title']='None'
    for title in df['cleaned_website_title']:
        if title == 'None':
            df['final_title'][i] = title
            i += 1
            continue
        try:
            pageUrl = "https://www.rottentomatoes.com/m/{}".format(title)
            page = requests.get(pageUrl)
            if page.status_code == 404:
                print('Status code 404 issue on: ', pageUrl)
                df['final_title'][i] = pageUrl
                i += 1
                continue
            # soup = bs(page.content, 'html.parser')
            df['final_title'][i] = title
            print("Found: ", pageUrl)
            i += 1
            # time.sleep(1)
        except:
            print('An error occured on: ', pageUrl)
            df['final_title'][i] = pageUrl
            i += 1
    csv_filepath = os.path.join(os.path.dirname(__file__), 'final_title_output.csv')
    df.to_csv(csv_filepath, index=False)

def id_score():
    critic_score = pd.read_csv('critic_score_output.csv')
    critic_id_score = critic_score[['id','critic_score']]
    csv_filepath = os.path.join(os.path.dirname(__file__), 'critic_id_score.csv')
    critic_id_score.to_csv(csv_filepath, index=False)


if __name__ == '__main__':
    # crawl_urls(clean_process())
    # scrape_urls()
    # recheck_urls()
    id_score()