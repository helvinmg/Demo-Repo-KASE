class Parent:
    def disp(self):
        print("Details from A")

class Child(parent):
        def disp(self):
            super().disp()
            #print("Details from B")

obj=Child()
obj.disp()#"Details from B"
#childs copy of disp will override parents disp
