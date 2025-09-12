# class Parent:
#     def m1(self):
#         print('This is m1 in parent')
#     def m2(self):
#         print('This is m2')
#
# class Child(Parent):
#     def m3(self):
#         print('this is m3')
#     def m1(self):
#         super().m1()
#         print('this is m1 in child')
#
#
#
# p=Parent()
# p.m1()
# p.m2()
#
# c=Child()
# c.m3()
# c.m1()

# class Company:
#     def __init__(self):
#         self.cname='luminar technolab'
#     def showCompany(self):
#         print('company name : ',self.cname)
#
# class Employee(Company):
#     def __init__(self):
#         # super().__init__()
#         Company.__init__(self)
#         self.name='arun'
#         self.age=21
#         self.empid=100
#         self.salary=2000
#     def getsalary(self):
#         print('salary : ',self.salary)
#
# e=Employee()
# e.getsalary()
# e.showCompany()


class Hospital:
    def __init__(self):
        self.hname = 'AIMS Kochi'
    def show_hospital(self):
        print('hospital : ', self.hname)
class Department:
    def __init__(self):
        self.dname='Oncology'
    def show_dept(self):
        print('department : ',self.dname)
class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.name='arun'
        self.age=21
        self.gender='male'
        self.admission_date='22-09-2025'
        self.bed_no=22
        self.discharge=''
    def full_Summ(self):
        print(self.name,self.age,self.gender,self.admission_date,self.bed_no)
        if(self.discharge!=''):
            print('status : ',self.discharge)
        else:
            print('status : not discharge')
        Hospital.show_hospital(self)
        Department.show_dept(self)
    def setdi(self):
        self.discharge=input("enter the discharge date : ")


p=Patient()
p.setdi()
p.full_Summ()