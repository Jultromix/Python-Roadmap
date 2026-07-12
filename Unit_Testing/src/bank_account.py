from datetime import datetime

from src.exceptions import InsufficientFundsError, WithdrawalTimeError


class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Account created")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited: {amount}, New Balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()

        if now.hour < 8 or now.hour > 17:  # Example condition, adjust as needed
            raise WithdrawalTimeError("Withdrawals are not allowed at this time.")

        if now.day in [6, 7]:  # Example condition for weekends
            raise WithdrawalTimeError("Withdrawals are not allowed on weekends.")

        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew: {amount}, New Balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Balance checked: {self.balance}")
        return self.balance

    def transfer(self, amount, target_account):
        if amount > 0:
            if self.balance < amount:
                self._log_transaction(
                    f"Failed transfer of {amount} to {target_account}, Insufficient funds"
                )
                raise InsufficientFundsError("Insufficient funds for transfer.")

            self.balance -= amount
            target_account.deposit(amount)
            self._log_transaction(f"Transferred: {amount}, New Balance: {self.balance}")
        return self.balance
