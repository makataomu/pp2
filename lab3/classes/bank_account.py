class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("deposit must be > 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Withdrawals may not exceed the available balance.")

account = BankAccount("Aldar kose", 1000)

account.deposit(500)
print(f"{account.owner}: {account.balance} tg")

account.withdraw(200)
print(f"{account.owner}: {account.balance} tg")

account.deposit(-100) 
print(f"{account.owner}: {account.balance} tg")

account.withdraw(1500)  
print(f"{account.owner}: {account.balance} tg")
