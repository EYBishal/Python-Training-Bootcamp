with open("notes.txt", "r") as s:
    content = s.read()

with open("backup.txt", "w") as d:
    d.write(content)
