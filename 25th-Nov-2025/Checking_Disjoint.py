
a={1,2,3}
b={3,5,6}
f=True
for i in a:
    if i in b:
        f=False
if f:
    print("Disjoint")
else:
    print("NOT disjoint")
