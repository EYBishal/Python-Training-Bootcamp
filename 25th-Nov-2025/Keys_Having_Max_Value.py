
marks = {"A": 85, "B": 92, "C": 78, "D": 92}
max_value = None
for key in marks:
    if max_value is None or marks[key] > max_value:
        max_value = marks[key]
for key in marks:
    if marks[key] == max_value:
        print(key)
