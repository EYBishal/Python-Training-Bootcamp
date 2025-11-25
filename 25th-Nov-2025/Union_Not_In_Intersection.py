a={1,2,3}
b={3,5,6}
c=a | b
d=a&b
f=True
e=set()
for i in c:
    if i not in d:

        e.add(i)
print(e)
print(c)
print(d)
