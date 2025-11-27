
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


person = ScholarAthlete("Bishal", "A+", "Football")
person.display()

################################################################


class Teacher:
    def teach(self):
        print("Teaching students...")

class ContentCreator:
    def create_content(self):
        print("Creating educational content...")

class OnlineTrainer(Teacher, ContentCreator):
    def start_session(self):
        print("Starting online training session...")
        self.teach()
        self.create_content()


trainer = OnlineTrainer()
trainer.start_session()


############################################################################



class HealthDevice:
    def track_health(self):
        print("Tracking health metrics...")

class NotificationDevice:
    def send_notification(self):
        print("Sending notifications...")

class SmartWatch(HealthDevice, NotificationDevice):
    def show_features(self):
        print("SmartWatch Features:")
        self.track_health()
        self.send_notification()

watch = SmartWatch()
watch.show_features()



