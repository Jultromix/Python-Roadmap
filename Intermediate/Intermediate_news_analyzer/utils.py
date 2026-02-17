def extract_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    return list(filter(lambda article: article["source"]["name"] == source, articles))


def get_reading_time(article: dict) -> dict:
    """Calculates the reading time"""
    minutes = len(article["content"]) // 200 + 1
    article["reading_time"] = minutes
    return article
