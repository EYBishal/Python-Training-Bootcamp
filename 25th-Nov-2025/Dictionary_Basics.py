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

#Remove
student.pop("city")
del student["age"]
print(student)
student.clear()

#print
for k in student.keys():
    print(k) #to get keys
for v in student.values():
    print(v) #to get values
for k,v in student.items():
    print(k,v)# to get both
