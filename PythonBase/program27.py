# created a function for retrun sum
def s(a,b):
    s=a+b
    return s

q=s(3,4)
print(q)

# created a function for retrun area of circle
def area(n):
    s=3.14*(n**2)
    return s

n=int(input("Enter the radius : "))
p=area(n)
print("Area : ",p)

# created a function for retrun armstrong
def armstrong(n):
    a=len(str(n))
    arm=0
    temp=n
    while n!=0:
        d=n%10
        arm += d**a
        n //=10
    if temp == arm :
        return True
    else:
        return False

n=int(input("enter the value : "))
q=armstrong(n)
print(q)

# position argument
def some(a,b):
    print(a)
    print(b)

some("ada",32)
some(32,"3faf")

# keyword argument
def some(a,b):
    print(a)
    print(b)

some(a="ada",b=32)
some(a=32,b="3faf")

#default argument
def fa(name,age=30):
    print(name)
    print(age)

fa('arun',42)
fa('kiran')

def fu(*args):
    print(args)

fu(323,3232,3232)
fu(1,2,3,4,5,5,6,2,2,9)


