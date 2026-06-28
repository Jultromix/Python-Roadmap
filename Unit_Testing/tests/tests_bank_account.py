import unittest, os

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

    def test_transaction_log(self):
        self.account.deposit(100)
        self.assertTrue(os.path.exists(self.account.log_file))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1

        self.account.deposit(100)
        assert (
            self._count_lines(self.account.log_file) == 2
        )  # Account creation and deposit

        # Verifying the log for transfers
        target_account = BankAccount(balance=500)
        self.account.transfer(200, target_account)
        assert target_account.get_balance() == 700
        assert self._count_lines(self.account.log_file) == 3

        with self.assertRaises(ValueError):
            self.account.transfer(20000, target_account)
            assert self._count_lines(self.account.log_file) == 4
