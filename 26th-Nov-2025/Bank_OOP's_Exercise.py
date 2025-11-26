class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


    def print_balance(self):
        print(self.name)
        print(self.balance)

bank=Bank("Bishal", 100)
bank.deposit(100)
bank.withdraw(10)
bank.print_balance()
