
data = {"a": 1, "b": 2, "c": 1}

inverted = {}

for key in data:
    value = data[key]
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]

print(inverted)
