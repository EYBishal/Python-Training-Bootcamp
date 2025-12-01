
def check():
    try:
        f = open("log.txt", "r")
        print(f.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")

check()
