for i in 'jfafafaf':
    print(i)

l=["3232","3",32323,"2aff23"]
for i in l:
    print(i)

d={'a':'faf','b':3}
for i in d:
    print(i)


s='python is a programming language'
vowels='aeiouAEIOU'
for i in s:
    if i not in vowels:
        print(i,end='')
print()
l=[25,86,32,32,76,342,856]
for i in l:
    if i>50:
        print(i ,end=' ')
print()
l=['red','green','orange','yellow','blue']
for i in  l:
    if len(i)<5:
        print(i,end=' ')
print()
d={'country1':'India','country2':'Nepal','country3':'NewZealand','country4':'Iceland','country5':'Australia'}
a='land'
for i in d.values():
    if a in i:
        print(i)

#Givem a list
l=['arun',34,'hello',9.8]
for i in l:
    if type(i)==str:
        print(i)

for i in range(1,11):
    print(i ,end=' ')
print()
for i in range(10,101,10):
    print(i ,end=' ')
print()
for i in range(8,-1,-2):
    print(i ,end=' ')
print()
for i in range(1,7):
    print(i**2 ,end=' ')
print()
for i in range(10,-2,-1):
    print(i ,end=' ')
print()
for i in range(-8,1,2):
    print(i ,end=' ')
sum=0
for i in range(1,21):
    sum +=i
print('sum : ',sum)

l=[11,34,67,23,90]
sum=0
for i in range(len(l)):
    if l[i]>50:
        sum+=l[i]
print('sum :',sum)

#Given a dictionary
d={'num1':46,'num2':89,'num3':60,'num4':12,'num5':67}
for i in d.values():
    if i%3==0:
        sum += i
print('sum of div 3 : ',sum)

#Given a dictionary
d={'arun':34,'amal':56,'anu':23,'kiran':32}
sum=0
l = len(d)
for i in d.values():
    sum+=i
print('average : ',sum/l)

#factorial of a number using for loop
fact=1
n=int(input("enter a number to find factorial : "))
for i in range (1,n+1):
    fact *=i
print('factorial : ',fact)
#factors of a number
n=int(input("enter the number to find factors : "))
for i in range(1,n+1):
    if n%i ==0:
        print('factors of',n,'is :', i)

#multiplication table of a number
n=int(input("enter the number to get multiplication table : "))
for i in range(1,11):
    print(i,'*',n,'=', i*n)
