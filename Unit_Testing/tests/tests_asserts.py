import unittest, requests, os
from dotenv import load_dotenv

SERVER = "server_b"

load_dotenv()
BASE_URL = os.environ.get("BASE_URL")


def is_api_available():
    try:
        answer = requests.get(BASE_URL)

        if answer.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        return False


class AllAssertstests(unittest.TestCase):
    @unittest.skip("work in progress, it'll be enabled later on")
    def test_skipt_assert(self):
        self.assertEqual("Hello", "Bye", "Strings are not equal")

    @unittest.skipIf(SERVER == "server_b", "skipped because we're not in the server")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)

    @unittest.skipUnless(is_api_available(), "API is not available")
    def test_latest_rates(self):
        r = is_api_available()
        self.assertEqual(r, True, "API is not available")
