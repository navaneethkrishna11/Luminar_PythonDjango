# class Books:
#     def __init__(self):
#         self.bookid=int(input("enter the book id : "))
#         self.title=input("enter the book title : ")
#         self.author=input("enter the author name : ")
#         self.page=int(input("enter the page : "))
#         self.price=int(input("enter the price : "))
#         self.language=input("enter the language : ")
#
#     def getauthor(self):
#         print("Author name : ",self.author)
#     def getprice(self):
#         print("Pricce : ",self.price)
#     def gettitile(self):
#         print('Title : ',self.title)
#     def setprice(self):
#         a=int(input("set the price : "))
#         self.price=a
#         self.getprice()
#     def setauthor(self):
#         a=input("set the author : ")
#         self.author=a
#         print('author: ',self.author)
#     def settitle(self):
#         a=input("set the title : ")
#         self.title=a
#         print('title : ',self.title)
#     def print(self):
#         print(self.author,self.price,self.title)
#
# b=Books()
# b.getauthor()
# b.getprice()
# b.gettitile()
# b.setprice()
# b.settitle()
# b.setauthor()
# b.print()
#
# b2=Books()
# b2.getauthor()
# b2.settitle()
# b2.getprice()
# b2.setprice()


#Area and Perimeter of circle
class Circle:
    def __init__(self):
        self.radius=int(input("enter the radius : "))
    def getarea(self):
        print("Area : ",3.14*self.radius**2)
    def getperimeter(self):
        print('Perimeter : ',2*3.14*self.radius)

c1=Circle()
c1.getarea()
c1.getperimeter()

c2=Circle()
c2.getarea()
c2.getperimeter()

#Bank acoount creation and money deposit,withdraw
class Account:
    def __init__(self):
        self.acctnumber=int(input("enter the id : "))
        self.acctname=input("enter the name : ")
        self.balance=int(input("enter the amount : "))
    def deposit(self):
        dep=int(input("enter the amount to deposit : "))
        self.balance=self.balance+dep
        print("balance : ",self.balance)
    def withdraw(self):
        wi=int(input("enter the amount to withdraw : "))
        self.balance=self.balance-wi
    def showbalance(self):
        print("Balance amount  : ", self.balance)

a=Account()
# a.deposit()
# a.withdraw()
# a.showbalance()
b=Account()
# b.deposit()
# b.showbalance()
l=[a,b]
for i in l:
    print(i.acctname,i.acctnumber,i.balance)