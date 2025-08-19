def s(a,b):
    s=a+b
    print(s)
s(3,4)


def simple(p,r,t):
    si=(p*r*t)/100
    print("simple : ",si)

a=int(input("enter the principal : "))
b=int(input("enter the rate : "))
c=int(input("enter the time : "))
simple(a,b,c)


def co(string,ch):
    count=0
    for i in string:
        if i==ch:
            count +=1
    print('Count : ',count)

s=input("enter the string : ")
c=input("count of the string : ")
co(s,c)