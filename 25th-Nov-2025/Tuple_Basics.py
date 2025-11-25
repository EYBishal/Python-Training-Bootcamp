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
