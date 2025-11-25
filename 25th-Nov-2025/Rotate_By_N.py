nums = [1, 2, 3, 2, 4, 1, 5, 1]
n=int(input("Enter the value of n"))
sd=0
for j in range(n):
    for i in range(0,len(nums)-1):
        sd = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = sd

print(nums)
