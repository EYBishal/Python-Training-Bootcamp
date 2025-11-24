#Exercise 1 — Simple Calculator

a = float(input("Enter a: "))
b = float(input("Enter b: "))
sum_result = a + b
difference = a - b
product = a * b
if b != 0:
    division = a / b
else:
    division = "Undefined (division by zero)"
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)

#Exercise 2 — Age in 2050

birth_year = int(input("Enter birth year: "))
age_in_2050 = 2050 - birth_year
print("Age in 2050:", age_in_2050)

#Exercise 3 — Area of a Rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area:", area)

#Exercise 4 — Even or Odd

number = int(input("Enter number: "))
if number % 2 == 0:
    print("Output: Even")
else:
    print("Output: Odd")

#Exercise 5 — Simple Login Check

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Login")