#Single Inheritance
class Emp:
    def disp(self):
        print("displaying details")

        
class Developer(Emp):
    pass

obj=Developer()#default constructor
obj.disp()#accessing parent method
    
