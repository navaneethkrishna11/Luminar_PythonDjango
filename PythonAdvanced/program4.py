# regex method to find beginning from a string
# Match function
import re
s="hello python hello"
m=re.match(r'h[a-z]+',s)
print('Object format : ',m)
if m:
    print('Print String Format :',m.group())
    print('Index postion : ',m.span())
    print('start Position : ',m.start())
    print('End position : ',m.end())
else:
    print('error!!')

# Search function
a=re.search(r'p[a-z]+',s)
b=re.findall(r'\bh[a-z]+\b',s)
print('Using FindAll : ',b)
if a:
    print('Search func : ',a.group())
else:
    print('Error!!')

# sub function
s='navanee@okasi.com and joppz@yabc.com'
m=re.sub(r'@[a-z]+','@gmail',s)
print('email checker : ',m)





