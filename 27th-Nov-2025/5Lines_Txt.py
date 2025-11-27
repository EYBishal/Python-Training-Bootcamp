with open("notes.txt", "w") as f:
    f.write("Hello World\n")
    f.write("My name is Bishal\n")
    f.write("My name is Bishal\n")
    f.write("My name is Bishal\n")
    f.write("My name is Bishal\n")


with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
