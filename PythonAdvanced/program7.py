#class and object... OOPS beginning
class Person:
    def __init__(self,n,a):  #constructor method to create and intialize object
        self.name=n   #initialize name to current object
        self.age=a

    def show(self):
        print(self.name,self.age)

p1=Person('Amritha P Shibu',20) #create a object for class, automatically call __init__
p2=Person('Navaneeth Krishna',22)
p1.show()
p2.show()



class Person:
    def __init__(self):
        self.name=input('enter name : ')
        self.age=int(input("enter the age : "))

    def show(self):
        print(self.name,self.age)

p1=Person()
p2=Person()
p1.show()
p2.show()

