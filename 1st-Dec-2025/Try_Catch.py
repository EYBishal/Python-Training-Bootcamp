try:
    num=int(input("Enter number"))
    print(10/num)
except ValueError:
    print("Error")
except ArithmeticError:
    print("Divide by zero")

##################################

try:
    f=open("log.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not exist")
finally:
    print("Closing operation completed")

#finally is use for memory management
#will be execute even if try executes error
