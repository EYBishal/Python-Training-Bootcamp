#Tuple is immutable meaning it cant be changed

numbers=(1,2,3)
names=("Bishal","James","Subham","Niket","Asad")
mixed=(10,"Hello",3.5,True)

print(numbers)
print(names)
print(mixed)

print(numbers[0])
print(names[-1])
print(names[1])

#count and index
print(numbers.count(2))
print(names.index("James"))

#print operations
print(numbers[1:4])
print(numbers[:3])
print(numbers[::-1])
print(numbers[2:])

#packing and unpacking
data=10,20,30
a,b,c=data
print(a,b,c)

#Nested tuple
emp=("John",32,("Kolkata","India"))
print(emp[2][0])

#Max and Min using Tuple
numbers=(10,20,30,40,50)
max=-100
min=100
for n in numbers:
    if n>max:
        max=n
    if n<min:
        min=n
print(max,min)
