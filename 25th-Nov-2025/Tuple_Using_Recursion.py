
data = (10, (20, 30), (40, (50, 60)))
i = 0
while i < len(data):
    item = data[i]
    if isinstance(item, int):
        print(item)
    else:
        data = item + data[i+1:]
        i = -1
    i += 1
