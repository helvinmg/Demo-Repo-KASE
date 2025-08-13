#Multiple Inheritance
class Par1:
    def disp(self):
        print("Par1 Display")
    def height(self):
        print("height: 6 feet")
    def eyes(self):
        print("eye color: brown")

class Par2:
    def disp(self):
        print("Par2 Display")
    def eyes(self):
        print("eye color: blue")

class Child(Par2,Par1):
    def disp(self):
        print("Child Display")

c1=Child()
c1.disp()
c1.eyes()
c1.height()

