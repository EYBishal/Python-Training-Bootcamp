def check(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print(c)
