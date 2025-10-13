class Accounts:
    def __init__(self,acctnumber,accname,balance):
        self.acctnumber = acctnumber
        self.accname=accname
        self.balance=balance
    def deposit(self):
        depo=int(input("enter the amount to deposit : "))
        self.balance +=depo
    def withdrwa(self):
        withdea=int(input("enter the amount to withdraw : "))
        if withdea>self.balance:
            print('Insufficeient balance! ')
        else:
            self.balance -=withdea
    def showblance(self):
        print("balance : ",self.balance)

class Bank:
    def __init__(self):
        self.accounts=[]
    def create(self):
        acctnumber = int(input("Enter the account number : "))
        accname = input("Enter the name : ")
        balance = int(input("Enter the amount : "))
        self.accounts.append(Accounts(acctnumber,accname,balance))

    def deposit(self):
        acn=int(input("enter the account number : "))
        for i in self.accounts:
            if i.acctnumber == acn:
                i.deposit()
                return

        print('no account !!')

    def withdraw(self):
        acn = int(input("Enter the account number: "))
        for i in self.accounts:
            if i.acctnumber == acn:
                i.withdrwa()
                return
        print("No account !!")

    def showbalance(self):
        acn = int(input("Enter the account number: "))
        for i in self.accounts:
            if i.acctnumber == acn:
                i.showblance()
                return
        print("No account !!")

    def accountsdata(self):
        for i in self.accounts:
            print(i.acctnumber,i.accname,i.balance)

b = Bank()
while 1:
    try:
        print("-----------------------")
        print('| \t\tBANK          |')
        print("-----------------------")
        print("| 1.Create an account |")
        print("| 2.Deposit           |")
        print("| 3.Withdraw          |")
        print("| 4.ShowBalance       |")
        print("| 5.Exit              |")
        print("-----------------------")
        ch=int(input("Choose :"))
        if ch==1:
            b.create()
        elif ch==2:
            b.deposit()
        elif ch==3:
            b.withdraw()
        elif ch==4:
            b.showbalance()
        elif ch==5:
            print('Thank u for using our bank,Have a nice day :) ')
            break
        elif ch==6:
            b.accountsdata()
        else:
            print("Invalid input ")
    except Exception as e:
        print(e)
    # finally:
    #     print('Thank u for using our bank,Have a nice day :) ')






