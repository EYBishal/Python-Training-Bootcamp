nums = [1, 2, 3, 2, 4, 1, 5, 1]
nums.sort()
nu = []

for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1] and nums[i] not in nu:
        nu.append(nums[i])
