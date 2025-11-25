nums=(1,2,3,4,-4,-9)
c=True
for i in range(0,len(nums)-1):
    if nums[i]>nums[i+1]:
        c=False
if c:
    print("OK")
else:
    print("NO")
