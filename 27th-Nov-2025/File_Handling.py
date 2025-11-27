
#to write a file
with open("sample.txt", "w") as f:
    f.write("Hello World\n")
    f.write("My name is Bishal\n")

# to read a file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
