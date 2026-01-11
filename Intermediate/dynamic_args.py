#### INTO THE ARGS THEORY ####
def ejemplo_args(api_key, *args):
    print(f"Api_key: {api_key} de tipo {type(api_key)}")
    print(f"Argumentos dinámicos {args} de tipo {type(args)}")


ejemplo_args("p1", "p2", "p3")
ejemplo_args("p1_1", "p1_2")
# ejemplo_args()


def dinamic_adder(*args):
    """funtion to add numbers"""
    try:
        print(f" Numbers to add {args} with result {sum(args)}")
    except TypeError:
        print("tipo de dato incorrecto, operación abortada, usa solo números")


dinamic_adder(1, 1)
dinamic_adder(1, 1, 3, 4, 5, 6, 7, 8, 9)
dinamic_adder(1, "1")
dinamic_adder(1, 2.3)


def dinamic_adder_compr(*args):
    """function to add numbers conditioning its type"""
    print(
        f"Numbers to add {args} with result {
            sum([x for x in args if isinstance(x, (float, int))])
        }"
    )


dinamic_adder_compr(1, 1)
dinamic_adder_compr(1, "1")


#### KWARGS ###
def ejemplo_kwargs(**kwargs):
    print(f" {type(kwargs)}")
    print(f" {kwargs}")
    print("=========")


ejemplo_kwargs(key="llave", value="valor", grade=3)

ejemplo_kwargs(api_key="DEMO", query="Python News", timout=30, retries=3)

ejemplo_kwargs(
    api_key="GUARDIAN", section="Sports", from_date="2026-01-10", timeout=30, retries=3
)


### NEW SET OF PRECTICAL EXAMPLES Dynamic Args + APIs####


API_KEY = "8a234dab6f894d6f8ee8d9aad5818d12"
BASE_URL = "https://newsapi.org/v2/everything"

# import requests
import json
import urllib.parse
import urllib.request


# Test function 1
def newsapy_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)
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


response_data = fetch_news("newapi", api_key=API_KEY, query="Electronics")

for article in response_data["articles"]:
    print(article["title"])
