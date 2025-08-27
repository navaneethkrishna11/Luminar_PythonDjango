n1=int(input("enter number 1 :"))
n2=int(input("enter number 2 :"))
n3=int(input("enter number 3 :"))
n4=int(input("enter number 4 :"))
# largest of 4 numbers
if(n1>n2 and n1>n3 and n1>n4):
    print("n1 is greatest")
elif(n2>n3 and n2>n4):
    print('n2 is greatest')
elif(n3>n4):
    print("n3 is greatest")
else:
    print("n4 is greatest")
# largest of three numbers
if(n1>n2 and n1>n3):
    print("one")
elif (n2>n3):
    print('two')
else:
    print('three')


