# check

print("Hello world")

#varaibles

x=112
y=12.7
z="Bishal"
print(x,y,z)

#calculation arithmetic operator
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)

#program to check print odd or even

while i <= 20:
    if i%2 == 0:
      print(i,"is even")
    else:
      print(i, "is odd")
   
#if-elif-else

m=int(input("Enter your mark "))
if(m>=80):
    print("You got A grade")
elif(m>=60):
    print("You got B grade")
elif(m>=40):
    print("You got C grade")
else:
    print("Failed in this Exam ")

# for loop iterator

for i in range(1,6):
    print("Number:", i)

# while loop iterator

c=1
while c <= 5:
    print("Count:",c)
    c+=1

 #Break

for i in range(10):
    if i==5:
        break
    else:
        print(i)

#continue

for i in range(10):
    if i==5:
        continue
    else:
        print(i)

#list
numbers=[1,23,3,4]
print(numbers)

names=["bishal","champak","jethalal"]
print(names)

mixed=["salt",12,False]
print(mixed)

fruits=["apple","orange","banana"]
print(fruits[0])
print(fruits[-1])
fruits.pop(1)

fruits.pop()