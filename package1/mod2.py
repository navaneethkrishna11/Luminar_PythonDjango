from package1 import mod1
mod1.pr()

# global variable
x=3
def a():
    f=3
    print(33333)

print(x)

def aa():
    global e
    e=999
    print(e)

aa()
print(e)

# nexted func
def outer():
    x=20
    print('outer function !!',x)
    def inner():
        y=30
        print("Inner function !!",x)
    inner()
    print()
outer()

# decorater
def dec(func):        #create a decorater
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap
@dec                 #call the decorater
def a(a,b):          #create the main func
    return a-b
print(a(3,2))      #print the func
print(a(9,3))

# decorater
def dec(func):        #create a decorater
    def wrap(a,b):
        if b!=0:
            return func(a,b)
        return 'err'
    return wrap
@dec                 #call the decorater
def a(a,b):          #create the main func
    return a/b
print(a(3,2))      #print the func
print(a(9,0))



