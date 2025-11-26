class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):

        if num1 == 0 or num2 == 0:
            
            return ("Divide by zero Error")

        else:
            return num1 / num2

cal=Calculator(1,2)
print(cal.add(1,2))
print(cal.subtract(1,2))
print(cal.multiply(1,2))
print(cal.divide(1,2))
print(cal.divide(2,0))

