# # Write a program to create a dictionary of vowels from a string and count their frequency
i=input("enter the string : ")
d={}
vowels="aeiouAEIOU"
for a in i:
    if a in vowels:
        if a in d:
            d[a]+=1
        else:
            d[a]=1
print(d)

i=input("enter the string")
d={}
vowels="aeiouAEIOU"
for a in i:
    if a in vowels:
        d[a]=i.count(a)
print(d)