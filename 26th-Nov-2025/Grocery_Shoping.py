class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def bill(self):
        sprice=0
        if self.quantity == 0.250:
            sprice=self.price/4
        elif self.quantity == 0.50:
            sprice=self.price/2
        elif self.quantity == 0.75:
            sprice=(self.price/2) + (self.price*0.25)
        else:
            sprice=self.price
        return sprice

n=int(input("Enter the number of items"))
Total=0
for i in range(n):
    name=str(input("Enter the item name"))
    price=int(input("Enter the item price"))
    quantity=float(input("Enter the item quantity"))
    product=Product(name,price,quantity)
    Total=Total+product.bill()


print(Total)
