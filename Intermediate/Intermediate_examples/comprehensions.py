sample_items = [
    {
        "title": "Python logra nuevo exito",
        "source": {"name": "Python Org"},
        "description": "Gran noticia",
        "category": "Technology",
    },
    {
        "title": "Sports",
        "source": {"name": "Deportiva"},
        "description": "Gran noticia",
        "category": "sports",
    },
    {
        "title": "Famous people",
        "source": {"name": "Exelcior"},
        "description": "Gran noticia",
        "category": "Social",
    },
    {
        "title": "Nasa expedition",
        "source": {"name": "El Universal"},
        "description": "Gran noticia",
        "category": "Astronomy",
    },
]


def extract_title_traditional(articles):
    """Extract titles using a for loop"""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


def extract_title(articles):
    """Extract titles using a for loop with comprehension notation"""
    return [article["title"] for article in articles if len(article["title"]) > 10]


def extract_title_summary(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 10
    }


print(extract_title_traditional(sample_items))
print("==========================")
print(extract_title(sample_items))
print("==========================")
print(extract_title_summary(sample_items))

print("==========================\nExercise\n")


def extract_title_trad_set(articles):
    title_set = set()
    for article in articles:
        if len(article["title"]) > 5:
            title_set.add(article["title"])
    return title_set


def extract_title_set(articles):
    return {article["title"] for article in articles if len(article["title"]) > 5}


print(extract_title_trad_set(sample_items))
print("==========================")
print(extract_title_set(sample_items))
print("==========================\nExercise Source Sets\n")


def extract_sources_trad_set(articles):
    source_set = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            source_set.add(article.get("source").get("name"))
    return source_set


def extract_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


print(extract_sources_trad_set(sample_items))
print("==========================")
print(extract_sources(sample_items))


def categorize_trad(articles):
    """This function categorie a structure to associate the articles related to each source"""
    sources = extract_sources(articles)
    results = {
        # KEY = Category :
        # VALUE = lista[articles]
    }

    for source in sources:
        if source not in results:
            results[source] = []
        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)
    return results


def categorize(articles):
    sources = extract_sources(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print("\n", categorize_trad(sample_items))
print("=====")
print(categorize(sample_items))
