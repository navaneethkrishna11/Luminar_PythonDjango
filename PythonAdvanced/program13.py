# method overlaoding can not directly apply on python
class A:
    def show(self,):
        print('code1')
    def show(self,a):
        print('code2')
    def show(self,a,b):
        print('code3')

a=A()
a.show(30,3)

# method overriding, mainly used to modify or extending parent function
class Parent:
    def show(self):
        print('this is parent')
class Child(Parent):
    def show(self):
        super().show()
        print('this is child class')

c=Child()
c.show()

# dendal method, use print(dir(int) to get all the dendul methods
class A:
    def __init__(self):
        self.x=int(input("enter the number : "))
    def __add__(self, other):
        return self.x +other.x
    def __sub__(self, other):
        return self.x-other.x
a=A()
b=A()
print(a+b)
print(a-b)


# abstract class
from abc import*

class A(abc):
    @abstractmethod
    def abstracmethodname():
        pass
    
