import unittest

from src.calculator import addition, division, multiplication, subtraction


class CalculatorTests(unittest.TestCase):
    def test_addition_positive_values_positive_result(self):
        assert addition(1, 2) == 3

    def test_subtraction_positive_values_positive_result(self):
        assert subtraction(100, 50) == 50

    def test_multiplication_positive_values_positive_result(self):
        assert multiplication(5, 4) == 20

    def test_division_positive_values_positive_result(self):
        assert division(10, 2) == 5

    def test_division_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            division(10, 0)
