
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i**2}\n")

print("Squares written to numbers.txt")
