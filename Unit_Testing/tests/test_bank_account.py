import unittest, os

from sys import path

path.append(".")
from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="test_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_positive_val_increase_balance(self):
        new_balance = self.account.deposit(55)
        self.assertEqual(new_balance, 1055, "the balance is not equal")

    def test_withdraw_positive_val_decrease_balance(self):
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 500, "the balance is not equal")

    def test_get_balance_returns_correct_value(self):
        balance = self.account.get_balance()
        self.assertEqual(balance, 1000, "the balance is not equal")

    def test_transfer_positive_val_transfers_funds(self):
        target_account = BankAccount(balance=500)
        new_balance = self.account.transfer(200, target_account)
        self.assertEqual(new_balance, 800, "the balance is not equal")
        self.assertEqual(target_account.get_balance(), 700, "the balance is not equal")
        with self.assertRaises(ValueError):
            self.account.transfer(2000, target_account)  # Insufficient funds

    def test_transaction_log_created(self):
        self.account.deposit(100)
        self.assertTrue(os.path.exists(self.account.log_file))

    def test_count_transactions_in_log(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)

        self.account.deposit(100)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

        # Verifying the log for transfers
        target_account = BankAccount(balance=500)
        self.account.transfer(200, target_account)
        self.assertEqual(target_account.get_balance(), 700)
        assert self._count_lines(self.account.log_file) == 3

        with self.assertRaises(ValueError):
            self.account.transfer(20000, target_account)
            assert self._count_lines(self.account.log_file) == 4
