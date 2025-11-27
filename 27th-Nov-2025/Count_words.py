with open("notes.txt", "r") as f:
    text = f.read()
    words = text.split()  #stores words as list
    print("Number of words:", len(words))
