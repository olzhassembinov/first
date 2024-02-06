class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal rejected.")

# Example usage:
account = BankAccount("John Doe", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(1000)  # This should fail due to insufficient funds