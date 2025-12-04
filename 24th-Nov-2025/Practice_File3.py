# Exercise 1 — Second Largest Number (Without Sorting)
nums = [23, 89, 12, 78, 55, 42]
largest = None
second = None
for x in nums:
    if largest is None or x > largest:
        second = largest
        largest = x
    elif x != largest and (second is None or x > second):
        second = x
print(second)

# Exercise 2 — Move All Zeros to the End
lst = [0, 3, 0, 5, 7, 0, 9]
nonzeros = []
zero_count = 0
for x in lst:
    if x == 0:
        zero_count += 1
    else:
        nonzeros.append(x)
for _ in range(zero_count):
    nonzeros.append(0)
print(nonzeros)

# Exercise 3 — Interchange First and Last Elements
arr = ['a', 'b', 'c', 'd', 'e']
if len(arr) > 1:
    arr[0], arr[-1] = arr[-1], arr[0]
print(arr)

# Exercise 4 — Extract Only Prime Numbers
nums = [10, 11, 12, 13, 17, 20, 23]
primes = []
for n in nums:
    if n > 1:
        is_prime = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            primes.append(n)
print(primes)

# Exercise 5 — Find All Indices of a Given Value
nums = [5, 2, 7, 5, 9, 5, 3]
value = 5
indices = []
for i, x in enumerate(nums):
    if x == value:
        indices.append(i)
print(indices)

# Exercise 6 — Create a New List of Squares (Without Comprehension)
inp = [2, 4, 6, 8]
squares = []
for x in inp:
    squares.append(x * x)
print(squares)

# Exercise 7 — Separate Even and Odd into Two Lists
nums = [10, 3, 5, 12, 8, 7, 1]
even = []
odd = []
for x in nums:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)
