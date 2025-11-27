#Single Inheritance

class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def Brand(self):
        print(self.brand)

class Car(vehicle):
    def __init__(self, brand, model, year,wheeler):
        super().__init__(brand, model, year)
        self.wheeler = wheeler

    def Wheeler(self):
        print(self.wheeler)


c=Car("Mercedes","ax13",2019,4)
c.Brand()
c.Wheeler()

###############################################

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def Display(self):
        print(self.name)
        print(self.price)


class ElectronicProduct(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def quant(self):
        print(self.quantity)


c = ElectronicProduct("Iphone", 52000,1)
c.Display()
c.quant()
