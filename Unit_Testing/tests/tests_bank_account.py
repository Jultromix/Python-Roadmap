import unittest
from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        new_balance = self.account.deposit(55)
        assert new_balance == 1055

    def test_withdraw(self):
        new_balance = self.account.withdraw(500)
        assert new_balance == 500

    def test_get_balance(self):
        balance = self.account.get_balance()
        assert balance == 1000

    def test_transfer(self):
        target_account = BankAccount(balance=500)
        new_balance = self.account.transfer(200, target_account)
        assert new_balance == 800
        assert target_account.get_balance() == 700
        with self.assertRaises(ValueError):
            self.account.transfer(2000, target_account)  # Insufficient funds
