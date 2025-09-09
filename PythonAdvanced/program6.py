# Multiple excpetion with showing type and msg in exception
flag=0
while flag==0:
    try:
        n1=int(input("enter value 1 : "))
        n2=int(input("enter value 2 : "))
        print(n1/n2)
        flag=1
    except ValueError as e:
        print(e)
        print(type(e))

    except ZeroDivisionError as er:
        print(er)
        print(type(er))
    except :
        print("other error")


