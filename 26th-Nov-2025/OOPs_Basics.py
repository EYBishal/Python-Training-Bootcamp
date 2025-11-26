
class student:
    pass # it allows class to exist without any definition
s1=student() #new -- new object created
s2=student()

##################################################################3

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
