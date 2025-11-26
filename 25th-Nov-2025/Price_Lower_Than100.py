
items = {"apple": 50, "banana": 120, "orange": 80, "mango": 150}
filtered = {}

for key in items:
    if items[key] >= 100:
        filtered[key] = items[key]

print(filtered)
