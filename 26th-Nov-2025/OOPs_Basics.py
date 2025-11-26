
class student:
    pass # it allows class to exist without any definition
s1=student() #new -- new object created
s2=student()

##################################################################

#self use here is object of current class , used to refer to this clas using this keyword
class Student:
    def __init__(self, name, age):#constructor
        self.name = name
        self.age = age

#object created
s3=Student(name="Bishal", age=20)
s4=Student(name="Arun", age=23)
print(s3.name)
print(s3.age)

###################################################################

#Class is created named car
#__init__ is construtor which runs automatically when a new object of class is created
#brand ,model,price are attributes of the class
class Car:
    def __init__(self, brand, model,price):
        self.brand=brand
        self.model=model
        self.price=price
#here display is a method of the class where it uses self to call the attributes
#Here self is required to so that the method can access the attributes of the object        
    def display(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)

#creating three cars objects
#so actually what happend here is we created object and passing the attributes
car1 = Car("BMW","Mercedes",20000)
car1.display()

##################################################################

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)
        #print(self.emp_id)


emp_1 = Employee(1, "Bishal", "Department A", 100)
emp_2= Employee(2, "Arun", "Department B", 200)

emp_1.display()
emp_2.display()

#################################################################
# created new methods to try out operations

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

##################################################################
#Calculator

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):

        if num1 == 0 or num2 == 0:
            
            return ("Divide by zero Error")

        else:
            return num1 / num2

cal=Calculator(1,2)
print(cal.add(1,2))
print(cal.subtract(1,2))
print(cal.multiply(1,2))
print(cal.divide(1,2))
print(cal.divide(2,0))

