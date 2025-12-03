#Exercise 6 

#Create a class Product with attributes name, price, quantity. Add a method to calculate the 
#total cost of all quantities. 
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

p = Product("Laptop", 50000, 2)

#Exercise 7 

#Create a class Customer with attributes name, age, city. Add a method that checks if the 
#customer is eligible for a loyalty program (age > 25). 

class Customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def is_eligible_for_loyalty(self):
        return self.age > 25


c = Customer("Bishal", 28, "Kolkc = Customer("Bishal", 28, "Kolkata")

#Exercise 8 
#Create a class BankAccount that supports deposit, withdraw, check balance, and displays 
#transaction logs.

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ₹{amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        return self.balance

    def show_transactions(self):
        return self.transactions


acc = BankAccount("Bishal")
acc.deposit(1000)
acc.withdraw(500)
printprint("Balance:", acc.check_balance())

#Exercise 9 
#Create a class Mobile with attributes brand, model, storage. Add a method to upgrade storage. 

class Mobile:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def upgrade_storage(self, new_storage):
        if new_storage > self.storage:
            self.storage = new_storage
            print(f"Storage upgraded to {self.storage}GB.")
        else:
            print("New storage must be greater than current storage.")



m = Mobile("Samsung", "Galaxy S21", 128)
m.upgrade_storage(256)

#Exercise 10 
#Create a class Student with three subject marks. Add methods for total, percentage, and grade 
#(A, B, C, D). 

class Student:
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def total(self):
        return self.mark1 + self.mark2 + self.mark3

    def percentage(self):
        return (self.total() / 300) * 100

    def grade(self):
        pct = self.percentage()
        if pct >= 80:
            return "A"
        elif pct >= 60:
            return "B"
        elif pct >= 40:
            return "C"
        else:
            return "D"


s = Student(85, 90, 80)
print("Total:", s.total())
print("Percentage:", s.percentage())
print("Grade:", s.grade())

