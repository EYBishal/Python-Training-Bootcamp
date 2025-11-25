#List_Basics

fruits=["apple","orange","banana"]
print(fruits[0])
print(fruits[-1])
fruits.pop(1)

fruits.pop()
print(fruits)

#List_Features

nums=[1,2,3,5]
print(nums[1:4])
print(nums[:3])
print(nums[2:])
print(nums[::-1])


#Some basic List Functions

nums=[1,2,3,5,6]
print(len(nums))
print(max(nums))
print(min(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)



#List_comprehension

nums=[1,2,3,4,5,6]
sq=[n*n for n in nums]
syq=[4*n for n in nums]
print(sq)
print(syq)

