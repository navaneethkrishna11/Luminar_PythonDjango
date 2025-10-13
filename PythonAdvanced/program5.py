# try:
#     a=int(input("enter a number : "))
#     b=int(input("enter a number : "))
#     print(a+b)
# except ValueError:
#     print('value error')
# else:
#     pass

import math
output=0
while output==0:
    try:
        n=int(input("enter the value : "))
        print(math.factorial(n))
        output=1
    except ValueError:
        print('valueError')

try:
    a=input("enter the file : ")
    n=open(a,'r')
    print(n.read())
except FileNotFoundError:
    print('File Does Not Exist')
else:
   f.close()

