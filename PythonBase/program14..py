# # wap to check whether a number is 2 digit ,3digit or 4 digit
n1=int(input("enter the number : "))
a= len(str(abs(n1)))
if a == 2:
    print("It is two digit number")
elif a == 3:
    print("It is 3 digit number")
elif a==4:
    print('it is 4 digit number')

# # wap artihemtic operation
a=int(input("enter number 1 : "))
b=int(input("enter number 2 : "))
ch = input("operation : ")
if(ch == '+'):
    print("sum",a+b)
elif ch=='-':
    print('sub',a-b)
elif ch=='*':
    print('pdt',a*b)
elif ch=='/':
    print("div",a/b)

# score=int(input("enter the score : "))
if 91<=score<=100 :
    print("Grade A")
elif 81<=score<=90 :
    print('Grade B')
elif 71<=score<=80:
    print('Grade C')
elif 61<=score<=70 :
    print('Grade D')
elif score<61  :
    print('Grade E')

# #wap to print the triangle is isosceles,equilateral or scalene
a =int(input("enter the side 1 : "))
b = int(input("enter the side 2 : "))
c = int(input("enter the side 3 : "))
if ( a==b and b==c):
    print('equlateral')
elif a!=b and a!=c and b!=c :
    print('scalene')
elif a==b or b==c or a==c:
    print('isoceles')

# #wap to print number of days in a month
month = input("enter the month : ")
if month == 'january':
    print(" days : 31")
elif month == 'february':
    print(" days : 28")
elif month == 'march':
    print(" days : 31")
elif month == 'april':
    print(" days : 30")
elif month=='may':
    print(" days : 31")
elif month == 'june':
    print(" days : 30")
elif month == 'july':
    print(" days : 31")
elif month =='august':
    print(" days : 31")
elif month == 'september':
    print(" days : 30")
elif month == 'october':
    print(" days : 31")
elif month == 'november':
    print(" days : 30")
elif month == 'december':
    print(" days : 31")

#do it with list , it is easierr.. make 3 list with common days and print it with input
l1=['january','march','may','july','august','october','decemeber']
l2=['february']
i=input("enter the month ")
if i in l1:
    print('31 days')
elif i in l2:
    print('28 days')
else:
    print('30 days')


