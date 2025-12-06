#1 Write a Python program to create a le named notes.txt and write 5 lines of text into it.
lines = [
    "Line 1: Hello, this is a note.",
    "Line 2: Python file handling is simple.",
    "Line 3: We are writing text lines.",
    "Line 4: This is the fourth line.",
    "Line 5: End of initial notes."
]

with open("notes.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
      
#2 Write a program to read and print the contents of notes.txt line by line

with open("notes.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i}: {line.rstrip()}")

#3 Write a program that appends a new line to an existing le notes.txt that says:
# "This is an appended line."


with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("This is an appended line.\n")

print("Appended a new line to notes.txt.")


#4 Write a program that counts the number of lines in a given file
filename = "notes.txt" 

line_count = 0
with open(filename, "r") as f:
    for _ in f:
        line_count += 1

print(line_count)


#5 Write a program that reads a le and counts the number of words in it

filename = "notes.txt"

word_count = 0
with open(filename, "r") as f:
    for line in f:
        words = line.split()  
        word_count += len(words)
print(word_count)




#6 Write a program to copy the contents of one le ( source.txt ) to another le ( backup.txt ).

with open("source.txt", "r") as src:
    with open("backup.txt", "w") as dst:
        dst.write(src.read())



#7 Write a program that reads a text le and prints only those lines that contain the word "Python" .

with open("notes.txt", "r") as f:
    for line in f:
        if "Python" in line:  
            print(line, end="") 



#8 Write a program to read a CSV le named students.csv and print name and marks of each student.


import csv

with open("students.csv") as f:
    for name, marks in csv.reader(f):
        print(name, marks)




#9 Write a program that writes the squares of numbers from 1 to 10 into a le ( numbers.txt ), one per
#line.


with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i**2}\n")

print("Squares written to numbers.txt")



#10 Write a log writer program using append mode that adds entries like:
#"2025-01-01 10:30:45 - Application started"
# Use the datetime module.


from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"{datetime.now()} - Application started\n")
