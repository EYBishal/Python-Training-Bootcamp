class Property:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display(self):
        print(self.name)
        print(self.value)

class Building(Property):
    def __init__(self, name, value, area):
        super().__init__(name, value)
        self.area = area

    def areasq(self):
        print(self.area)


class Aparment(Building):
    def __init__(self, name, value, area, type):
        super().__init__(name, value,area)
        self.type = type


    def finalprice(self):
        print(self.type)

a=Aparment("T-TOWER",12000000,"1200sqft","2BHK")
a.display()
a.areasq()
a.finalprice()

###############################################################


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def type_of_animal(self):
        print("Name:", self.name, "| Age:", self.age)

class Mammal(Animal):
    def __init__(self, name, age, favfood):
        super().__init__(name, age)
        self.favfood = favfood

    def food(self):
        print("Favorite Food:", self.favfood)

class Dog(Mammal):  # Dog inherits from Mammal
    def __init__(self, name, age, favfood, found):
        super().__init__(name, age, favfood)
        self.found = found

    def display(self):
        self.type_of_animal()
        self.food()
        print("Found:", self.found)

# Create object
d = Dog("Sheru", 12, "Pet Food", "Everywhere")
d.display()
