class Mobile:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def update(self,storag):
        self.storage+=storag
        print(self.storage)

s=Mobile("Mobile",123,100)
s1=str(input("Do you want to update storage"))
if s1=="Yes":
    i=int(input("Enter choice"))
    s.update(i)
