import unittest
from tests_bank_account import BankAccountTests


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(descriptions=True, verbosity=1)
    runner.run(bank_account_suite())
