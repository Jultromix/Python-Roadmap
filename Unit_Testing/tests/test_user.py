import os
import unittest
from src.users import User
from faker import Faker
from src.bank_account import BankAccount


class UserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def tearDown(self) -> None:
        for account in self.user.accounts:
            if os.path.exists(account.log_file):
                os.remove(account.log_file)

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name_generated, email_generated)
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)
        self.assertEqual(user.accounts, [])

    def test_add_accounts_for_user(self):
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=0, max=1000),
                log_file=self.faker.file_name(extension="txt"),
            )
            self.user.add_account(account=bank_account)
        self.assertEqual(len(self.user.accounts), 3)

        expected_total = self.user.get_total_balance()
        self.assertEqual(
            sum(account.get_balance() for account in self.user.accounts), expected_total
        )
