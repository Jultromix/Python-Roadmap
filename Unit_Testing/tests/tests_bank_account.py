import unittest
from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount()
        assert account.deposit(55) == 55

    def test_withdraw(self):
        account = BankAccount(balance=1000)
        new_balance = account.withdraw(500)
        assert new_balance == 500

    def test_get_balance(self):
        account = BankAccount(balance=1000)
        balance = account.get_balance()
        assert balance == 1000
