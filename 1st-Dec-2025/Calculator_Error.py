
def calculator(op,a,b):
    try:
        if op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            print(a/b)
        else:
            print("Invalid operator")
    except ZeroDivisionError:
        print("Division by zero")
    except TypeError:
        print("Invalid operator")

calculator("+",1,2)
calculator("#",1,2)
