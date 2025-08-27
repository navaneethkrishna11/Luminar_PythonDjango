# extract all email using map()func
phone_book={
    'john':['111111111','john@gmail.com'],
    'bob':['222222222','bob@gmail.com'],
    'tom':['333333333','tom@gmail.com'],
}
print('Using map : ',(list(map(lambda x:x[1],phone_book.values()))))
# count of floating point values
l=[10,'hello',9.8,'abc',11.2,'arun']
a=[i for i in l if type(i)==float]
print('Using list : ',len(a))
print('Using filter : ',len(list(filter(lambda x:type(x)==float,l))))

# importing a custom module
import mod1
mod1.hello()
mod1.s(1,2)

from mod1 import *
hello()
s(2,3)


