#1. Write a program that reads a string and prints the number of vowels, consonants, and digits.
'''
s=input("Enter any String")
v=0
c=0
d=0
for i in s.lower():
    if i in 'aeiou':
        v+=1
    elif i in '0123456789':
        d+=1
    elif i in'bcdfghjklmnpqrstvwxyz':
        c+=1
print("Vowel count is ",v)
print("Consonant count is ",c)
print("Digit count is ",d)
'''
#2. Create a function that takes a sentence and returns a dictionary of word frequencies.

'''
def words(s):
    w=s.lower().split()
    d={}
    for i in w:
        d[i]=d.get(i,0)+1
    return d
s="Hello Hello I am Under the Water"
print(words(s))
'''



#3. Implement a mini calculator with add, subtract, multiply, and divide using functions.
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def calculator():
    s=input("Your choice of operation \n 1-- Add \n 2-- Sub  \n 3-- Mul  \n 4-- Div \n")
    a=int(input("Enter your number"))
    b=int(input("Enter your number"))
    if s=="add":
        print(add(a,b))
    elif s=="sub":
        print(sub(a,b))
    elif s=="mult":
        print(mul(a,b))
    elif s=="div":
        print(div(a,b))
    else:
        print("Invalid operation")
calculator()
'''



#4. Write a program that reads N numbers and returns the second highest value without sorting.
'''
li=[]
i=int(input("Enter your number to fill"))
for i in range(i):
    a=int(input("Enter your number"))
    li.append(a)
max1=-1000
max2=-1000
for i in li:
    if i>max1:
        max2=max1
        max1=i
    elif i<max1 & i>max2:
        max2=i
print(max2)
'''


#5. Read 10 values and store them into a list without using loops (use list comprehension).

'''
count=10
numbers = [
    int(input(f"Enter number {i+1}: "))
    for i in range(count)
]
print(numbers)
'''
