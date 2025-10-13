# find the longest string
s="python is a programming language"
d={}
count=0
for i in s.split():
    d[i]=len(i)
ma=max(d,key=d.get)
print('Method 1 :',ma)
ma_l=max([len(i) for i in s.split()])
for i in s.split():
    if len(i) == ma_l:
        print('method 3 :',i)

w=""
l=0
for i in s.split():
    if len(i)>l:
        w=i
        l=len(i)
print('Method 2 :',w,l)

# find max value from the list
l=[12,45,67,89,23]
l.sort()
print("max value method 1 : ",l[-1])
l=[12,45,67,89,23]
m=l[0]
for i in l:
    if i>m:
        m=i
print('max value method 2: ',m)
for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print('Bubble sort :',l[-1])

# lambda function
s=lambda a,b:a+b
print(s(3,3))

d={'name':'arun','age':30}
a=lambda x: d['name']
print(a(d))

l=['book','john',300,'english']
b=lambda x:l[1]
print(b(l))

# define a lambda function to add 3 numbers
s=lambda a,b,c:a+b+c
print(s(1,2,1))

# define a function to find  a cube of a number
q=lambda a:a**3
print(q(6))

l=[1,3,5,2]
print(list(map(lambda x:x**3,l)))
print(set(map(lambda x:x**3,l)))
print(tuple(map(lambda x:x**3,l)))

#create a list of cubes from the given list
a=[1,2,3,4]
print(list(map(lambda x:x**3,a)))
#create a list of names
l=[{'name':'arun','age':23},{'name':'amal','age':24},{'name':'anu','age':26}]
print(list(map(lambda x:x['name'],l)))
#create a list of authors
d=[['book1','john',200],['book2','mike',300],['book3','sam',500]]
print(list(map(lambda x:x[1],d)))
#create a list of length
colors=['red','green','orange','yellow','blue']
print(list(map(lambda x:len(x),colors)))
#create of list of square roots
l=[36,81,49,16,82]
print(list(map(lambda x:x**0.5,l)))
print(list(filter(lambda x:x%2==0,l)))

#create a list of odd values
print('odd : ',list(filter(lambda x:x%2!=0,l)))
#create a list of numbers greater than 50
print('greater than 50 : ',list(filter(lambda x:x>50,l)))
#create of list of numbers that are divisible by 3
print('divisble by 3 : ',list(filter(lambda x:x%3==0,l)))
#create a list of even numbers
print("list of even and greater than 50 : ",list(filter(lambda x:x%2==0 and x>50,l)))

import functools
l=[36,81,49,16,82]
print('list reduced to : ',functools.reduce(lambda x,y:x+y,l))

l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
#sum of positive even numbers
s=sum([i for i in l if i>0 and i%2==0 ])
print(s)
