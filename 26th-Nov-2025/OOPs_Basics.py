
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
