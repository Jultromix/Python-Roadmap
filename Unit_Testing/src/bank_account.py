class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        if amount > 0:
            if self.balance < amount:
                raise ValueError("Insufficient funds for transfer.")

            self.balance -= amount
            target_account.deposit(amount)
        return self.balance
