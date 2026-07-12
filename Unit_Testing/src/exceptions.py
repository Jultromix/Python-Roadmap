class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds in the bank account."""

    pass


class WithdrawalTimeError(Exception):
    """Custom exception for withdrawals made outside of allowed hours."""

    pass
