import unittest
from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount()
        assert account.deposit(55) == 55
