'''
Polymorphism
1.Method Overloading - No
2.Operator Overloading - Yes '''
class Emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def disp(self):
        print(f"{self.name} {self.salary}")
    def __add__(self,other):
        return self.salary+other.salary
    def __gt__(self,other):
        return self.salary>other.salary
    def __eq__(self,other):
        return "Not possible ti check"

emp1=Emp("vikas",45000)
emp2=Emp("manohar",55000)
emp1.disp()
emp2.disp()
print(emp1+emp2)
print(emp1>emp2)
print(emp1==emp2)
