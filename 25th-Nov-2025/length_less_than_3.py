names=["bishal","shubham","niket","lo"]
for i in range(len(names)):
    if len(names[i])<3:
        names.pop(i)
print(names)
