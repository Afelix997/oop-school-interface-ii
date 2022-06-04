from .person import Person 
import csv

class Staff(Person):
    def __init__(self, name, age, role, password,employee_id):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
    
    def all_staff():
        staff_list=[]
        with open('/mnt/c/Users/angel/OneDrive/Desktop/Code-Platoon/homework/wk_2/day_4/oop-school-interface-i/data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                staff_list.append(row)
        return staff_list 