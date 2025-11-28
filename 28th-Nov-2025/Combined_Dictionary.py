
d1 = {
    "name": "bishal",
    "age": 12,
    "roll": 123
}

d2 = {
    "name": "bi",
    "age": 12,
    "rolli": 123
}

combined = {}

for key in set(d1.keys()).union(d2.keys()):
    if key in d1 and key in d2:
        combined[key] = [d1[key], d2[key]]
    elif key in d1:
        combined[key] = d1[key]
    else:
        combined[key] = d2[key]

print(combined)
