
import csv

def check():
    try:
        with open("order.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error: File not found.")
    except csv.Error:
        print("Error: Incorrect file format.")

check()
