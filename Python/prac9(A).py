#write a python to implement the concepts of oops such as type of methods inheritance and polymorphism #program to use such as class in  static
class student:
    #constructor
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    #instance method
    def disp(self):
        print("Student name: ",self.name)
        print("Student roll: ",self.roll)
class User:
    #static method
    def show(s):
        print("User name: ",s.name)
        print("User roll: ",s.roll)
        s.disp()
st=student("Amit",1001)
User.show(st)

        
