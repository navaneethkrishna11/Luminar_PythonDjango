# INHERITENCE SINGLE LEVEL
# SUPER() HELPS TO MODIFY AND EXTEND PARENT CLASS FUNCTION
class Person:
    def __init__(self):
        self.name=input("enter the name : ")
        self.age=int(input("enter the age : "))
    def show(self):
        print(self.name)
        print(self.age)

class Child(Person):
    def __init__(self):
        super().__init__()
        self.place=input("enter the place : ")

    def show(self):
        super().show()
        print(self.place)

c=Child()
c.show()