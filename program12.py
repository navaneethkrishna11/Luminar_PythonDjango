#wpa to check even or not
num1=int(input("enter the number : "))
if num1%2==0:
    print("even")
else:
    print("odd")

# write a program whether a number is 3 digit number or not
num1=int(input("enter the number : "))
if(len(str(num1))==3):
    print("it is 3 digit number")

# wap to check whether the last digit of numer is multiple of 3 or not
num1=int(input("enter the number : "))
a=num1%10
if(a%3==0):
    print('the last digit is multiple of 3')
else:
    print("not")

# wap to check whether an entererd charcter is vowel or not
ch=input("enter the character : ")
vow='aeioAEIOU'
if ch in vow:
    print("it is vowel")
else:
    print('not vowel')

# check whether the enterd number is present in the lsit
l=[23,56,89,12,60]
n=int(input("enter the number : "))
if n in l:
    print("the number is present")
else:
    print("it is nt prsent")

# wap to check whether an entered name is present in dict or not
d={'name':'arun','age':25,'place':'ekm'}
name1=input('enter the name : ')
if name1 in d.values():
    print("the name is present in the dict")
else:
    print("the name is not present in the dict")

  # wap to check whether two entered strings are equal or not
a=input("enter string 1 : ")
b=input("enter string 2: ")
if a == b:
    print("strings are equal")
else:
    print("not equal")

# wap to check whether the given string is palindrom or not
a=input("enter the string : ")
if a == a[::-1]:
    print('palindrome')
else:
    print('not palindrome')

# wap to check find maximum of two number
a=int(input("enter the number 1 :"))
b=int(input("enter the number 2: "))
print(max(a,b))

