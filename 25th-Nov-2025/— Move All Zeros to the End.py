nums=[0,30,5,7,0,9]
n=[]
c=0
for i in nums:
    if i%2==0:
        c+=1
    else:
        n.append(i)
for i in range(c):
    n.append(0)
print(n)
