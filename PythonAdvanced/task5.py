# Check whether two strings are anagram or not without using built in function
s1=input("enter the string 1: ")
s2=input("enter the string 2: ")
d1={}
d2={}
for i in s1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1

for i in s2:
    if i in d2:
        d2[i] += 1
    else:
        d2[i] = 1

# print(d1,d2)
if d1==d2:
    print('anagram')
else:
    print('not')




