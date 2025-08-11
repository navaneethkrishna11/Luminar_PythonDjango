s="hello guyss"
for i in s:
    if i=='l':
        break
    print(i)
print()
s="hello guyss"
for i in s:
    if i=='l':
        continue
    print(i)

s="Python is a programming langugage"
ch=input("enter the character : ")
for i in s:
    if i == ch:
        print(i)
        break
    print(i)


fruits=['banana','apple','orange','pineapple','mango']
for i in fruits:
    if i =='pineapple':
        break
    print(i,end=" ")
print()
for i in fruits:
    if i =='apple':
        continue
    print(i ,end=' ')
print()
l=[45,67,12,90,78,10]
for i in l:
    if i%3==0:
        continue
    print(i)

colors=['red','green','orange','blue','black','yellow']
for i in colors:
    if 'b' in i[0]:
        print(i)
        break