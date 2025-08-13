#Hierarchical Inheritance
class Emp:
    def test(self):
         print("Test is working")
    def disp(self):
        print("displaying details from Emp Class")
class Developer(Emp):
    def disp(self):
         print("displaying details from Developer")
class Tester(Emp):
    def disp(self):
         print("displaying details from Tester")

dev1=Developer()
dev1.test()
dev1.disp()

tes1=Tester()
tes1.test()
tes1.disp()
