#Emp Class
class Emp:
    org_name="ABC Limited"
    def __del__(self):
        print("destructor working")
    def __init__(self,name="test",age=30,desg="test",sal=5000):
        self.name=name
        self.age=age
        self.desg=desg
        self.salary=sal
    def empDisp(self):
        print(f"{self.name} {self.age} {self.desg} {self.salary}")
    def empIncSalary(self,perc):
        self.salary=self.salary+self.salary*perc/100
    def empPromotion(self,newdesg):
        self.desg=newdesg

employees=[]
for i in range(2):
    name=input("enter the name: ")
    age=int(input("enter the age: "))
    salary=float(input("enter the salary: "))
    desg=input("enter the desg: ")
    empobj=Emp(name,age,salary,desg)
    employees.append(empobj)

for emp in employees:
    emp.empDisp()

del employees[0]
'''
empobj=Emp("amal",29,"HR",60000)
empobj.empDisp()
empobj.empIncSalary(10)
empobj.empPromotion("Senior HR")
empobj.empDisp()
'''
    
