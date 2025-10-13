#Regex expression
import re
s="""John is 18 and Sam is 20
Mike is 40 and Kalis is 87
"""
names=re.findall(r'[A-Z][a-z]+',s)
print("List of Names : ",names)
ages=re.findall(r'[0-9]{2}',s)
print("List of Ages : ",ages)

s="abcc abc abde abce abcccccs abdceee"
a=re.findall(r'abc*',s)
print(a)

s="sat pat cat rat mat bat"
# words starting with s,p,r and end 'at'
a=re.findall(r'[spr]at',s)
print(a)

# find all words strging eith expect s,p,r and ends at at
b=re.findall(r'[^spr]at',s)
print(b)

# given a string find 3,4,5 letters word from the string
s="the quick brown fox jumps over the lazy dog"
c=re.findall(r'\w{3,5}',s)
print(c)

# given a string s='123 1234 12345 123456 1234567 12345678'
s='123 1234 12345 123456 1234567 12345678'
# find 3,4,5 digit number from the string
d=re.findall(r'\b[0-9]{3,5}\b',s)
print(d)

s='hello world $hello world _hello world_ 1hello world :hello world'
e=re.findall(r'\bhello\b',s)
print(e)
