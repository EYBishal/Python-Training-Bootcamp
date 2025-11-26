class Bank:
    def __init__(self, name, balance, log):
        self.name = name
        self.balance = balance
        self.log=[]
#here f helps us to insert variable directlyinside a string using {} it is string literal
    def deposit(self, amount):
        self.balance += amount
        self.log.append(f"deposited {amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.log.append(f"withdrawn {amount}")

    def check_balance(self):
        print(self.balance)

    def show_logs(self):
        for t in self.log:
            print(t)


s=Bank("Bank", 100, "log")
s.deposit(100)
s.withdraw(10)
s.check_balance()
s.show_logs()
