class Customer:
    def __init__(self, name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def loyalty(self):
        if self.age >= 25:
            print("You are eligible for loyalty Program")
        else:
            print("You are eligible for loyalty Program")

c=Customer("Bishal", 25, "California")
c.loyalty()
