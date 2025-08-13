#OOPS in python
class Student:
    #creating instance attributes
    def __init__(self):
        self.branch="cs"
        self.college="abc college"

stud1=Student()
print("Stud1 details:",stud1.branch,stud1.college)
stud2=Student()
print("Stud2 details:",stud2.branch,stud2.college)
