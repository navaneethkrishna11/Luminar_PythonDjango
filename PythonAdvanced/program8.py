class Employee:
    def __init__(self):
        self.empid=int(input("employee id : "))
        self.name=input("enter the name : ")
        self.age=int(input("enter the age  : "))
        self.place = input("enter the place : ")
        self.salary=int(input("enter the salary : "))
        self.designation = input("enter the designation : ")
    def showdetails(self):
        print('Name of employee :',self.name,'\n','Age of employee : ',self.age,'\n','Place of employee : ',self.place,'\n','empid : ',self.empid)
    def getSalary(self):
        print('Salary : ',self.salary)


e1=Employee()
e1.showdetails()
e1.getSalary()
