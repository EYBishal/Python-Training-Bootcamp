mixed=("banana","apple","mango",1,2,3)
num=()
st=()
for i in range(0,len(mixed)-1):
    if type(mixed[i])==int:
        num+=(mixed[i],)
    else:
        st+=(mixed[i],)
print(st)
print(num)
