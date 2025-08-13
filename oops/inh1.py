#Single Inheritance
class Emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("displaying details from parent")
        print(f"{self.name} {self.age}")
        
class Developer(Emp):
    def __init__(self,name,age,project,salary):
        super().__init__(name,age)#invoking par constructor
        self.project=project
        self.salary=salary
    def disp(self):
         print("displaying details from child")
         print(f"{self.name} {self.age} {self.project} {self.salary}")
obj=Developer("Manu",30,"MERN App",45000)
obj.disp()
    
