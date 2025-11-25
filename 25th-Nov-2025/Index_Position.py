mixed=("banana","apple","mango")
n=input("Enter to check position")
for i in range(0,len(mixed)-1):
    if n==mixed[i]:
        print(i)
        break
    else:
        if i==len(mixed)-1:
            print("NO")
