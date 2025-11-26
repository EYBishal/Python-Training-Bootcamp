
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {}
for key in dict1:
    merged[key] = dict1[key]
for key in dict2:
    if key in merged:
        if isinstance(merged[key], list):
            merged[key].append(dict2[key])
        else:
            merged[key] = [merged[key], dict2[key]]
    else:
        merged[key] = dict2[key]

print(merged)
