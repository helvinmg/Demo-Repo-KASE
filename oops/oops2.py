class Student:
    #class attributes
    semester=5
    college="NES College Calicut"
    def __init__(self,rollno,name):#parameterized contructor
        self.rollno=rollno#instance attributes
        self.name=name
    def __del__(self):
        print("destructor is working")
    def display(self):#method
        print(f"RollNo.={self.rollno} Name={self.name}")
        print(f"Sem={Student.semester} College={Student.college}")

stud1=Student(1,"arun")
stud1.display()
stud2=Student(2,"manu")
stud2.display()
Student.college="NESE College Calicut"
stud1.display()
stud2.display()
del stud1
