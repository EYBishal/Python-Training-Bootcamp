nums=[[1,2],[3,4],[5,6],[7,8],[9]]
nu=[]
for i in nums:
    if type(i)==list:
        for j in i:
            nu.append(j)
    else:
        nu.append(i)

print(nu)
