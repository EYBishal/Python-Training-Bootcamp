numbers=(10,20,30,40,50)
max=-100
min=100
for n in numbers:
    if n>max:
        max=n
    if n<min:
        min=n
print(max,min)
