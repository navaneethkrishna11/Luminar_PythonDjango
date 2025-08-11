#write a program to display positive or negative number
a=int(input("enter : "))
if(a>0):
    print('postive')
else:
    print('negative')
#write a program to display a number if number is multiple of 3
num1=int(input("enter a number : "))
if(num1%3==0):
    print('multiple of 3')
else:
    print('not multiple of 3')
#write a program to display a number if number is multiple of 3 and 4
num1=int(input("enter a number : "))
if(num1%3==0 and num1%4==0):
    print('multiple of 3 and 4')
else:
    print('not multiple of 3 and 4')

# writ a program to display name if the entered name contains n
name=input("enter a name :")
n='n'
if n in name:
    print("it have n in name")


#write a program to dispaly name if the last first character of name is 'a'
name=input("enter :")
if name[0]=='a':
    print("it have first letter a")
else:
    print('it dont have a ')
#write a program to dispaly name if the last last character of name is 'a'
name = input("enter a nanme : ")
if name[-1]=='a':
    print('the last character have a')
else:
    print('the last character dont have a')

#write a program to display if the 'location' contains word 'land'
location=input("enter the word : ")
if('land' in location):
    print("yes")
else:
    print('not')
