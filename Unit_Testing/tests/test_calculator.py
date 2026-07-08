import unittest

from src.calculator import addition, division, multiplication, subtraction


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        assert addition(1, 2) == 3

    def test_subtraction(self):
        assert subtraction(100, 50) == 50

    def test_multiplication(self):
        assert multiplication(5, 4) == 20

    def test_division(self):
        assert division(10, 2) == 5

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            division(10, 0)
