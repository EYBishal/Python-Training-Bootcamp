def conversion(li):
    for i in li:
        try:
            print(int(i))
        except ValueError:
            print("Not possible")


li=["Bishal",12,"3","#",1234]
conversion(li)
