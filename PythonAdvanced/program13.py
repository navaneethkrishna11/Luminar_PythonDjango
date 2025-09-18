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

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Recatangle(Shape):
    def __init__(self):
        self.x=10
        self.y=10
    def area(self):
        print('area : ',self.x*self.y)
    def perimeter(self):
        print("perimeter : ",2*(self.x*self.y))
class Circle(Shape):
    def __init__(self):
        self.r=30
    def area(self):
        print('area : ',3.14*self.r**2)
    def perimeter(self):
        print('perimeter : ',4*3.14*self.r)

r=Recatangle()
r.area()
r.perimeter()
c=Circle()
c.area()
c.perimeter()