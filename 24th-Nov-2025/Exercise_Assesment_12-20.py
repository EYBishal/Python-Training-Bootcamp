#Exercise 12 — Square & Cube of a Number

number = int(input("Enter number: "))
square = number * number
cube = number * number * number
print("Square:", square)
print("Cube:", cube)

#Exercise 13 — Convert Minutes to Hours & Minutes


total_minutes = int(input("Enter minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(hours, "hours and", minutes, "minutes")

#Exercise 14 — Swap Two Variables

a = int(input("Enter a: "))
b = int(input("Enter b: "))
a = a + b
b = a - b
a = a - b
print("After swap → a =", a, ", b =", b)

#Exercise 15 — Check Positive, Negative, or Zero


number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Exercise 16 — Find the Last Digit of a Number

number = int(input("Enter a number: "))
last_digit = number % 10
print("Last digit:", last_digit)

#Exercise 17 — Sum of First N Natural Numbers

N = int(input("Enter N: "))
sum_n = 0
for i in range(1, N + 1):
    sum_n += i
print("Output:", sum_n)

#Exercise 18 — Multiplication Table

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

#Exercise 19 — Count Digits in a Number

number = int(input("Enter a number: "))
count = 0
while number > 0:
    number = number / 10
    count += 1  
print("Total digits:", count)

#Exercise 20 — Reverse a Number (Logic Basics)


number = int(input("Enter a number: "))
reversed_number = 0
while number > 0:
    last_digit = number % 10  
    reversed_number = reversed_number * 10 + last_digit  
    number = number // 10  
print("Output:", reversed_number)