class Animal:
    def speak(self):
        print("Animal makes a sound")
#inheritance example
#here the animal class is passed to dog so that it can acces the methods of parent class
class Dog(Animal):
    def bark(self):
        print("Dog makes a sound")

d=Dog()
d.speak()
d.bark()

########################################################

class Person:
    def __init__(self, name):
        self.name = name

#super() keyword is use to acces the constructor of the parent as child uses it from inheritance

class child(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

e=child("Bishal",10)
print(e.name,e.age)
