#module is a .py file contaning related functions
#recursive function to find factorial
pi=3.14

def findFact(num=5):
    if num==1:
        return 1
    else:
        return num*findFact(num-1)

def testEve(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
