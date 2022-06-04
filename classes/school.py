from .person import Person 
from .student import Student
from .staff import Staff 

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff() 
        self.students = Student.all_students()

    def list_students(self):
        count=1
        print("All Students:")
        for dic in self.students:
            print(f"{count}. {dic['name']} {dic['school_id']}")
            count+=1
    def find_student_by_id(self,id_num):
        for dic in self.students:
            if dic['school_id'] == id_num:
                return dic


            
        

