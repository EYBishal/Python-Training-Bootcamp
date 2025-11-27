
from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"{datetime.now()} - Application started\n")
