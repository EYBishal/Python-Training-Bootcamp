def check():
    try:
        f=open("log.txt","a")
        s=input("Enter your name")
        f.write(s)
        f.close()
    except FileNotFoundError:
        print("File not exist")
    else:
        print("Executed as succesful completion of try block")
    finally:
        print("Exercise Completed")

check()
