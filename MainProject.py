
class StudentDatabase:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_all_students(self):
        return self.students
    
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.get_id() == student_id:
                return student
        return None


    
class Student:
    
    def __init__(self,student_id, name, department):
        # private the attributes
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False

    def enroll_student(self):
        if self.__is_enrolled:
            print("Already enrolled")
        else:
            self.__is_enrolled = True
            print("Enrolled successfully")
            
    def drop_student(self):
        if not self.__is_enrolled:
            print("Not enrolled")
        else:
            self.__is_enrolled = False
            print("Dropped successfully")
    
    def view_student_info(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        # i use ternary opertor here
        print(f"Enrolled: {"Yes" if self.__is_enrolled else "No"}")
        
        
    def get_id(self):
        return self.__student_id
        
        
        
# Student(1,"Siyam Hossain","CSE")
# Student(2,"Rasel Mahmud","CSE")


studentData = StudentDatabase()




# this methods are call from selection area
def addNewStudent():
    student_id = int(input("Student ID: "))
    if studentData.find_student_by_id(student_id):
        print("Error: ID already exist")
        return
    
    name = input("Name: ")
    department = input("Department: ")
    newStudent = Student(student_id, name, department)
    studentData.add_student(newStudent)
    print("Added Successfully")

def enroll_student():
    print("----------------------------")
    print("       Want to enroll       ")
    print("----------------------------")
    student_id = int(input("Student ID: "))
    found_student = studentData.find_student_by_id(student_id)
    if found_student:
        found_student.enroll_student()
    else:
        print("Not found")
        
        
def drop_student():
    print("----------------------------")
    print("        Want to drop        ")
    print("----------------------------")

    student_id = int(input("Student ID: "))
    found_student = studentData.find_student_by_id(student_id)
    if found_student:
        found_student.drop_student()
    else:
        print("Not found")
        
def view_all_students():
    students = studentData.get_all_students()
    if not students:
        print("Not found in database")
        return
    print("\n")
    print("----------------------------")
    print("         All Students       ")
    print("----------------------------")
    for student in students:
        student.view_student_info()
        print("----------------------------")
    
    

def Menu():
    while True:
        print("\n")
        print("---------------------------")
        print("        DataBase Menu      ")
        print("---------------------------")

        # 1. View All Students
        # 2. Enroll Student
        # 3. Drop Student
        # 4. Exit


        print("0. Add some Student first")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        print("---------------------------")
        
        select = input("Select: ")
        
        if select == "0":
            addNewStudent()
        elif select == "1":
            view_all_students()
        elif select == "2":
            enroll_student()
        elif select == "3":
            drop_student()
        elif select == "4":
            print("Exiting............")
            break
        else:
            print("Invalid selection! Try again")
                
Menu()   
    
        
        