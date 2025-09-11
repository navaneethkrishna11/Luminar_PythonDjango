#B A N K  O P E R A T I O N S
class Bank:
    def __init__(self):
        # self.acctnumber=0
        # self.acctname=""
        # self.balance=0
        self.accounts = []

    def create(self):
        try:
            acctnumber=int(input("enter the number :  "))
            for i in self.accounts:
                if acctnumber == i[0] :
                    print('Already account exist with that number!')
                    return

            acctname = input("enter user name : ")
            balance = int(input("enter the balance : "))
            self.accounts.append([acctnumber,acctname,balance])
            print('Account created successfully !!')
        except Exception as e:
            print(e)

    def deposit(self):
        try:
            acctnumber=int(input("enter the account number : "))
            for i in self.accounts:
                if  i[0] == acctnumber:
                    dep=int(input("enter the amount to deposit : "))
                    i[2]+=dep
                    print('Successfully deposited!!')
                    return

            print('No Account Found!!')
        except Exception as e:
            print(e)

    def withdraw(self):
        try:
            acctnumber = int(input("enter the account number : "))
            for i in self.accounts:
                if i[0] == acctnumber:
                    wi = int(input("enter the amount to withdraw : "))
                    a = i[2] - wi
                    if a < 0:
                        print('Account doesn’t have that much amount!')
                        return
                    else:
                        i[2] -= wi
                        print('Successfully withdrawn!!')
                        return

            print('No Account Found!!')
        except Exception as e:
            print(e)

    def showbalance(self):
        acctnumber = int(input("enter the account number : "))
        for i in self.accounts:
            if i[0] == acctnumber:
                print('Balance of AcctNumber',i[0],'is amount :',i[2])
                return

        print('No Account Found in this Account Number !')

    def accountsdata(self):
        print('Account users : ')
        for i in self.accounts:
            print('| Account number : ',i[0],'| User name : ',i[1],'| Account balance :',i[2])


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

