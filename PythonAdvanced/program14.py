# a program using abstract class, in this created a abstract class emply , and with
# respect to it salary is inputed and printed.
from abc import *
class Employee(ABC):
    def __init__(self):
        print('Empolyee Data')
        self.empid=int(input("enter empid : "))
        self.name=input("enter the name : ")
        self.age=int(input("enter the age : "))
    @abstractmethod
    def getsalary(self):
        pass

class Fixedsalary(Employee):
    def __init__(self):
        super().__init__()
        self.mnthy=int(input("enter the salary monthly : "))
    def getsalary(self):
        print("salary : ",self.mnthy)
class Hoursalary(Employee):
    def __init__(self):
        super().__init__()
        self.hr=int(input("Enter the hour : "))
        self.rate=int(input("enter the rate : "))
    def getsalary(self):
        print('salary : ',self.hr*self.rate)

b=[]
while 1:
    print("1.Add Employee 2.Salary Details of perticular Emp 3.Exit")
    ch=int(input("enter the choice : "))
    if ch==1:
        print('1.fixed salary 2.hr salary :')
        t=int(input("choose : "))
        if t==1:
            e=Fixedsalary()
        elif t==2:
            e=Hoursalary()
        else:
            print('no option')
        b.append(e)
    elif ch==2:
        s = int(input("Enter the empid : "))
        found = False
        for e in b:
            if s == e.empid:
                e.getsalary()
                found = True
                break
        if not found:
            print("Not Found!!")
    elif ch==3:
        break
    else:
        print('Invalid input!')