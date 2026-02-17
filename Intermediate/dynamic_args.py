### NEW SET OF PRECTICAL EXAMPLES Dynamic Args + APIs####
import json
import urllib.parse
import urllib.request
from dotenv import load_dotenv
import os

from Intermediate_news_analyzer.utils import (
    extract_sources,
    get_articles_by_source,
    get_reading_time,
)
from open_ai import analize_news_with_ai


load_dotenv()
API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL")

# import requests


class NewsSystemError(Exception):
    """General Errors in the app"""

    pass


class APIKeyError(NewsSystemError):
    """Error for invalid key"""

    pass


# Test function 1
def newsapy_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError("An error occured, API's connection failed")
    return f"NewsAPI: {query} con timout {timeout}"


# Test function 2
def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timout {timeout}"


def fetch_news(api_name, *args, **kwargs):
    """
    Funcion flexible para conectar con API
    """

    base_config = {"timeout": 30, "retries": 3}

    custom_config = {
        **base_config,
        **kwargs,
    }

    api_clients = {"newapi": newsapy_client, "guardian": guardian_client}

    client = api_clients[api_name]
    return client(*args, **custom_config)


response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"{e}")

if response_data:
    for article in response_data["articles"]:
        print(article["title"])

if response_data:
    print(analize_news_with_ai(response_data["articles"], "Qué piensas de Python?"))


if response_data:
    sources_set = extract_sources(response_data["articles"])

    for index, source in enumerate(sources_set, start=1):
        print(f"No: {index} -- {source}")

    sources_set = extract_sources(response_data["articles"])

    for index, source in enumerate(sources_set, start=1):
        print(f"No: {index} -- {source}")

    articles = list(map(get_reading_time, response_data["articles"]))

    analize_news_with_ai(response_data["articles"], "What do you think about python?")

    for article in articles:
        print(f" {article['title']} -- Reading time {article['reading_time']}")

    journal_articles = get_articles_by_source(
        response_data["articles"], "Yahoo Entertainment"
    )
    print(journal_articles)
