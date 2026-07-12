import requests
import os
from dotenv import load_dotenv

load_dotenv()
RATE_URL = os.environ.get("RATE_URL")
IP_FREEIPAPI_URL = os.environ.get("IP_FREEIPAPI_URL")  # This is the api being used
IP_IPAPI_URL = os.environ.get("IP_IPAPI_URL")  # An alternative API


def get_rates(country):
    url = f"{RATE_URL}?base={country}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def get_location(ip):
    url = f"{IP_FREEIPAPI_URL}{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # import ipdb
    # ipdb.set_trace()  # Debugging breakpoint, press q to exit
    return {
        "country": data["countryName"],
        "city": data["cityName"],
        "continent": data["continent"],
        "countrycode": data["countryCode"],
    }


example = get_rates("USD")

if __name__ == "__main__":
    print(get_location("8.8.8.8"))
