s="python is a programming language"
d={}
count=0
for i in s.split():
    d[i]=len(i)
ma=max(d,key=d.get)
print(ma)

w=""
l=0
for i in s.split():
    if len(i)>l:
        w=i
        l=len(i)
print(w,l)


# find max value from the list
l=[12,45,67,89,23]
l.sort()
print("max value method 1 : ",l[-1])
l=[12,45,67,89,23]
m=l[0]
b=[]
for i in l:
    if i>m:
        m=i
print('max value method 2: ',m)
for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print('Bubble sort :',l[-1])









