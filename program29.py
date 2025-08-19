# # built in functions of strings
# s="python is programming"
# ch=input("enter the character")
# print(" index : ", s.index(ch))
# c=input("count : ")
# print("counted : ",s.count(c))

# count of words into a dict
s="hello world"
d={}
for i in s:
    if i!=" ":
     d[i]=s.count(i)

print(d)

# length of string more than 5
s='python coding is easy and fun'
for i in s.split():
    if len(i)>5:
        print(i,end=" ")
print()