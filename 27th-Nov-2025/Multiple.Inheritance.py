
class Father:
    def __init__(self, lname):
        self.lname = lname

class Mother:
    def __init__(self, qualities):
        self.qualities = qualities

class Child(Father, Mother):
    def __init__(self, lname, qualities, name):
        Father.__init__(self, lname)   # Explicit call
        Mother.__init__(self, qualities)
        self.name = name

    def display(self):
        print(self.name, self.lname, self.qualities)

c = Child("Bhattacharjee", ["honesty", "hardworking"], "Bishal")
c.display()

########################################################


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_student_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def show_athlete_info(self):
        print(f"Sport: {self.sport}")

class ScholarAthlete(Student, Athlete):  # Multiple Inheritance
    def __init__(self, name, grade, sport):
        Student.__init__(self, name, grade)   # Explicit call
        Athlete.__init__(self, sport)

    def display(self):
        self.show_student_info()
        self.show_athlete_info()
        print("This person excels in both academics and sports!")

# Create object
person = ScholarAthlete("Bishal", "A+", "Football")
person.display()
