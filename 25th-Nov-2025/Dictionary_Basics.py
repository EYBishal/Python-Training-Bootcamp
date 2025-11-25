#Dictionary --- Stores structured Data

student={
    "name":"Bishal",
    "age":24,
    "city":"Kolkata"
}

#to get data
print(student["name"])
print(student["age"])
print(student.get("name"))

#Adding key value pair or Updating pair

student["email"]="bishal@gmail.com"
student["city"]="Asansol"

print(student)
