import unittest
from src.api_client import get_location
from unittest.mock import patch
import requests


class ApiClientTests(unittest.TestCase):
    @patch("src.api_client.requests.get")
    def test_get_location_returns_correct_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "cityName": "Mountain View",
            "continent": "North America",
            "countryCode": "US",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA", "Country should be USA")
        self.assertEqual(
            result.get("city"), "Mountain View", "City should be Mountain View"
        )
        self.assertEqual(
            result.get("continent"),
            "North America",
            "Continent should be North America",
        )
        self.assertEqual(
            result.get("countrycode"),
            "US",
            "Country code should be US",
        )
        mock_get.assert_called_once_with("https://free.freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "cityName": "Mountain View",
                    "continent": "North America",
                    "countryCode": "US",
                },
            ),
        ]
        # mock_get.return_value.status_code = 200       #These are part of the side effect
        # mock_get.return_value.json.return_value = {
        #     "countryName": "USA",
        #     "cityName": "Mountain View",
        #     "continent": "North America",
        #     "countryCode": "US",
        # }

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA", "Country should be USA")
        self.assertEqual(
            result.get("city"), "Mountain View", "City should be Mountain View"
        )
        self.assertEqual(
            result.get("continent"),
            "North America",
            "Continent should be North America",
        )
        self.assertEqual(
            result.get("countrycode"),
            "US",
            "Country code should be US",
        )
