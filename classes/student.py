from .person import Person 
import csv

class Student(Person):
    def __init__(self, name, age, role, password,school_id):
        Person.__init__(self, name, age, password, role)
        self.age = age
        self.password = password
        self.role = role
        self.school_id = school_id

    def all_students():
        student_list=[]
        with open('/mnt/c/Users/angel/OneDrive/Desktop/Code-Platoon/homework/wk_2/day_4/oop-school-interface-i/data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student_list.append(row)
        return student_list 
    def __str__(self):
        return f"{self.name.upper()}\n------\nAge: {self.age}\nID: {self.school_id}"
        

