import pytest
from src.bank_account import BankAccount


def test_addition():
    a = 2
    b = 4
    assert a + b == 6


@pytest.mark.parametrize(
    "amount, expected_value", [(100, 1100), (200, 1200), (3000, 4000)]
)
def test_deposit_multiple_values(amount, expected_value):

    account = BankAccount(balance=1000, log_file="test_log.txt")
    new_balance = account.deposit(amount)
    assert new_balance == expected_value
