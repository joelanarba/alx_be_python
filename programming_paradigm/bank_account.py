class BankAccount:
    def __init__(self, initial_balance=0):
        # Initializes the account balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Add money to the account
        self.account_balance += amount

    def withdraw(self, amount):
        # Take money out if enough funds are available
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Show current account balance
        print(f"Current Balance: ${self.account_balance:.2f}")