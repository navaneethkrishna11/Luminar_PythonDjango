# def add():
#     a=int(input("enter first values : "))
#     b=int(input("enter the second value : "))
#     s=a+b
#     print("sum : ",s)
#
# add()

#define a function find factorial of a number
def factor():
    n1=int(input("enter the number : "))
    fact=1
    while n1>0:
        fact=fact*n1
        n1-=1
    print("factorial : ",fact)

factor()

#define a function to find reverse of a number
def reverse():
    n=int(input("enter the number : "))
    a=n
    rev=0
    while n!=0:
        a=n%10
        rev=rev*10+a
        n //=10
    print("Reverse : ",rev)

reverse()

#Define a function to check whether a number is prime or not
def prime():
    n1=int(input("enter the value  "))
    if n1<=1:
        return false
    else:
        is_p=True
        for i in range(2,n1):
            if n1%i==0:
                is_p=False
        if is_p:
            print("Prime")
        else:
            print("not prime")
prime()

#Define a function to find the BMI value
def bmi():
    weight = int(input("Weight in kg "))
    height = int(input("Height in cm  "))
    bmi=weight/(height/100)**2
    print("BMI",bmi)

bmi()