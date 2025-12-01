def safe_list(a,l):
    try:
        return (l[a])
    except IndexError:
        return "Error list index out of range"

li=[1,2,3,4,56,7,9]

print(safe_list(12,li))
print(safe_list(2,li))
