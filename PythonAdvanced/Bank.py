#B A N K  O P E R A T I O N S
class Bank:
    def __init__(self):
        self.acctnumber=0
        self.acctname=""
        self.balance=0
        self.accounts = []
    def create(self):
        self.acctnumber=int(input("enter the number :  "))
        self.acctname =input("enter user name : ")
        self.balance=int(input("enter the balance : "))
        self.accounts.append([self.acctnumber,self.acctname,self.balance])
    def deposit(self):
        acctnumber=int(input("enter the account number : "))
        for i in self.accounts:
            if  i[0] == acctnumber:
                dep=int(input("enter the amount to deposit : "))
                i[2]+=dep
                print('Successfully deposited!!')
            else:
                print('No Account Found!! Create Account')
    def withdraw(self):
        acctnumber = int(input("enter the account number : "))
        for i in self.accounts:
            if i[0] == acctnumber:
                wi=int(input("enter the amount to withdraw : "))
                i[2]-=wi
                print('Successfully withdraw!!')
            else:
                print('No Account Found!! Create Account')
    def showbalance(self):
        acctnumber = int(input("enter the account number : "))
        for i in self.accounts:
            if i[0] == acctnumber:
                print('Balance of AcctNumber ',i[0],'is amount :',i[2])
            else:
                print('No Account Found in this Account Number !')

    def accountsdata(self):
        print('Account users : ')
        for i in self.accounts:
            print('| Account number : ',i[0],'| User name : ',i[1],'| Account balance :',i[2])

b = Bank()
while 1:
    try:
        print("---------------------")
        print('\t\tBANK')
        print("---------------------")
        print(" 1.Create an account \n 2.Deposit \n 3.Withdraw \n 4.ShowBalnce \n 5.Exit")
        print("------------------")
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
            break
            exit
        elif ch==6:
            b.accountsdata()
        else:
            print("Invalid input ")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except:
        print('error!')
    finally:
        print('Thank u for using our bank,Have a nice day :) ')


