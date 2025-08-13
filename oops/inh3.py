#MultiLevel Inheritance
class Emp:#Grandparent
    def login(self):
        print("Login Successful")
    def disp(self):
        print("displaying details from Emp")
class Developer(Emp):#parent
    def debug(self):
        print("Bebugging in process")
    def disp(self):
         super().disp()
         print("displaying details from Developer")
class Intern(Developer):#child
    def learn(self):
        print("Learning how to make bugs")
    def disp(self):
         super().disp()
         print("displaying details from intern")

obj=Intern()
obj.login()
obj.debug()
obj.learn()
obj.disp()
    
