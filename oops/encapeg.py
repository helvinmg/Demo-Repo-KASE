#Encapsulation
class User:
    def __init__(self,name,password,log):
        self._username=name#protected
        self.__password=password#private
        self.log=log#public
    def userDetails(self):
        print("Details from userDetails")
        print("Username=",self._username)
        print("Password=",self.__password)
        print("Log=",self.log)

user1=User("alvin","alvin@123","12-08-25")
user1.userDetails()
print(user1.log)
print(user1._username)
print(user1.__password)
