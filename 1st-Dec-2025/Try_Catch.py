try:
    num=int(input("Enter number"))
    print(10/num)
except ValueError:
    print("Error")
except ArithmeticError:
    print("Divide by zero")
