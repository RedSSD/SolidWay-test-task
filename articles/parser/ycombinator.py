import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

from articles.parser.db import add_article_to_db

YCOMBINATOR_NEWS_URL = 'https://news.ycombinator.com/'
REGEX_ARTICLE_URL = (
    r"\b((?:(https?|ftp):\/\/)?(?:www\.)?(?:[-a-zA-Z0-9@:%._\+~#=]{1,256}\."
    r"[a-zA-Z0-9()]{1,6}\b)(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*))\b"
)
REGEX_YCOMBINATOR_ARTICLE_URL = r"(?:[?&])(\w+)=([^&]+)"
TIME_LIMIT = 15


def article_parser_ycombinator():

    print(f"{datetime.now()} - INFO - parser started")

    try:
        response = requests.get(YCOMBINATOR_NEWS_URL + "newest")
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.RequestException
    ) as exception:
        print(f"{datetime.now()} - EXCEPTION - {exception}")
        return

    if response.status_code != 200:
        print(f"{datetime.now()} - RESPONSE ERROR - status code {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # get a list of <tr> tags that contain article data
    article_elements = soup.body.center.table.find_all('tr')[3]

    # get a list of <tr> tags which contain article headline and url
    articles = article_elements.find_all('tr', class_='athing')

    # get a list of <span> tags which contain article publication time
    articles_time_element = article_elements.find_all('span', class_='age')

    for article, article_time in zip(articles, articles_time_element):
        article_td_element = article.find_all("td", class_="title")[1]
        article_title = article_td_element.a.text
        article_link = article_td_element.a['href']
        article_publication_time = article_time.a.text

        # ignore videos (as we need only articles)
        if "[video]" in article_title:
            continue

        if "minutes" not in article_publication_time or int(article_publication_time[0:2]) > TIME_LIMIT:
            continue

        article_publication_time = int(article_publication_time[0:2])

        # If it is a ycombinator article the url will be "?id=...". In this case parser adds ycombinator news url
        if not re.findall(REGEX_ARTICLE_URL, article_link) and re.findall(REGEX_YCOMBINATOR_ARTICLE_URL, article_link):
            article_link = YCOMBINATOR_NEWS_URL + article_link

        if add_article_to_db(article_title, article_link):
            print(f'{datetime.now()} - INFO - ADDED "{article_title}"')
