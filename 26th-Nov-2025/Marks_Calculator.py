class Student:
    def __init__(self, m1, m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1+self.m2+self.m3

    def average(self):
        return (self.m1+self.m2+self.m3)/3

    def percentage(self):
        return (self.m1+self.m2+self.m3)/3


s1=Student(100,90,80)
s2=Student(90,90,90)
print(s1.total())
print(s2.total())
print(s1.average())
print(s2.average())
print(s1.percentage())
print(s2.percentage())
