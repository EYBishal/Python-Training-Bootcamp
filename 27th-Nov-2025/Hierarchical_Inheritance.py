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
