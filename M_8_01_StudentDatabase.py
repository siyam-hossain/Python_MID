"""
    1. Create the StudentDatabase class
    
    Define a class named StudentDatabase with one class attribute named student_list. Initially, it should be an empty list. Create a class method add_student() to insert an object of the Student class into student_list.

"""


class StudentDatabase:
    student_list = []
    
    def add_sudent(self,name):
        self.student_list.append(name)
        
    def view_student(self):
        print(*self.student_list)

student = StudentDatabase()
student.add_sudent("Siyam Hossain")
student.view_student()
        
