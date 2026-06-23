import unittest
from src.calculator import addition, subtraction


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        assert addition(1, 2) == 3

    def test_substraction(self):
        assert subtraction(100, 50) == 50
