try:
    num=int(input("Enter number"))
    print(10/num)
except ValueError:
    print("Error")
except ArithmeticError:
    print("Divide by zero")

##################################

#with finally

try:
    f=open("log.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not exist")
finally:
    print("Closing operation completed")

#finally is use for memory management
#will be execute even if try executes error

#####################################

#with else

try:
    value =int("50")
except ValueError:
    print("Please enter a number")
else:
    print("successful conversion",value)


########################################

#raise

def check_age(age):
    if age < 18:
        raise ValueError("Age must be greater than or equal to 18")
    return "Allowed"

print(check_age(18))

#raise here allows to throw error according to us


##############################################3

#custom exception
#here lowbalance.... inherits the exception class
class LowBalanceError(Exception):
    pass
def withdraw(amount,balance):
    if amount> balance:
        raise LowBalanceError("Insufficient Balance")

    return balance-amount


print(withdraw(105,101))

