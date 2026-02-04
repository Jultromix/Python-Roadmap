#### INTO THE ARGS THEORY ####
def ejemplo_args(api_key, *args):
    print(f"Api_key: {api_key} de tipo {type(api_key)}")
    print(f"Argumentos dinámicos {args} de tipo {type(args)}")


ejemplo_args("p1", "p2", "p3")
ejemplo_args("p1_1", "p1_2")
# ejemplo_args()


def dinamic_adder(*args: int | float) -> float:
    """
    Add multiple numbers dynamically and print the result.

    This function accepts a variable number of numeric arguments,
    calculates their sum, and prints both the input numbers and
    the calculated result to the console.

    Args:
        *args (int | float): Variable number of numeric values to be added.
            Can be integers or floating-point numbers.

    Returns:
        float: The sum of all provided numbers. Returns 0 if no arguments
            are provided.

    Raises:
        TypeError: If any argument is not a number (int or float).
            The function catches this error and prints a user-friendly
            message in Spanish instead of raising the exception.

    Examples:
        >>> dinamic_adder(1, 2, 3)
        Numbers to add (1, 2, 3) with result 6

        >>> dinamic_adder(1.5, 2.5, 3.0)
        Numbers to add (1.5, 2.5, 3.0) with result 7.0

        >>> dinamic_adder(10, 20)
        Numbers to add (10, 20) with result 30

        >>> dinamic_adder("text", 5)
        tipo de dato incorrecto, operación abortada, usa solo números
    """
    try:
        result = sum(args)
        print(f"Numbers to add {args} with result {result}")
        return result
    except TypeError:
        print("tipo de dato incorrecto, operación abortada, usa solo números")
        return 0.0


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


API_KEY = ""
BASE_URL = ""

# import requests
import json
from types import NoneType
import urllib.parse
import urllib.request


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
    response_data = fetch_news("newapi", api_key=API_KEY, query="Electronics")
except APIKeyError as e:
    print(f"{e}")

if response_data:
    for article in response_data["articles"]:
        print(article["title"])
