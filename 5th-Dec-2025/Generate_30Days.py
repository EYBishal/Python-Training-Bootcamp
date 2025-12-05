from datetime import date, timedelta

li = [(date.today() + timedelta(days=i)) for i in range(30)]
print(li)
