
import csv

with open("students.csv") as f:
    for name, marks in csv.reader(f):
        print(name, marks)
