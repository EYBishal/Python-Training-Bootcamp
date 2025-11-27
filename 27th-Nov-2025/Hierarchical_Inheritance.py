class A:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def dis(self):
        self.display()
        print(self.age)

class C(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def dis(self):
        self.display()
        print(self.age)

b=B("Bishal",12)
b.dis()
c=C("Jim",12)
c.dis()

####################################################################################


class Animal: 
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

class Cow(Animal):
    def speak(self):
        print(f"{self.name} moos.")


dog = Dog("Sheru")
cat = Cat("Kitty")
cow = Cow("Gauri")

dog.speak()
cat.speak()
cow.speak()



####################################################################

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account No: {self.account_number}, Balance: {self.balance}")
s
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate}%")

class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: {self.overdraft_limit}")

class SalaryAccount(Account):
    def __init__(self, account_number, balance, employer_name):
        super().__init__(account_number, balance)
        self.employer_name = employer_name

    def display_info(self):
        super().display_info()
        print(f"Employer: {self.employer_name}")


print("=== Account Hierarchy ===")
savings = SavingsAccount("SA123", 5000, 4.5)
savings.display_info()

current = CurrentAccount("CA456", 10000, 2000)
current.display_info()

salary = SalaryAccount("SAL789", 15000, "ABC Corp")
salary.display_info()


##############################################################


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def make_payment(self):
        print(f"Processing payment of {self.amount}")

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def make_payment(self):
        print(f"Paid {self.amount} using Credit Card {self.card_number}")

class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def make_payment(self):
        print(f"Paid {self.amount} using UPI ID {self.upi_id}")

class WalletPayment(Payment):
    def __init__(self, amount, wallet_name):
        super().__init__(amount)
        self.wallet_name = wallet_name

    def make_payment(self):
        print(f"Paid {self.amount} using Wallet {self.wallet_name}")

print("\n=== Payment Hierarchy ===")
credit = CreditCardPayment(2500, "1234-5678-9876")
credit.make_payment()

upi = UPIPayment(1500, "bishal@upi")
upi.make_payment()

wallet = WalletPayment(500, "Paytm")
wallet.make_payment()

