# common elements
l1=[12,45,67,89,90]
l2=[34,78,12,56,45]
a=set(l1)
b=set(l2)
print(a.intersection(b))
print(max(l1))

# find second largest element from the list
l=[12,45,67,89,90]
print('max : ',max(l))
l.sort()
print('second largest : ',l[-2])

#find the minimum element from the list
l=[12,45,67,89,90]
print('Minimum : ',min(l))

#find the second smallest element from the list
l=[1,1,2,3,3,3,5,6,7,7]
l.sort()
print("second smallest : ",l[1])

# create dictionary where keys are numbers and values are count of each number
l=[1,1,2,3,3,3,5,6,7,7]
d={}
for i in l:
    d[i]=l.count(i)
print(d)

#Given , find max slaary
d={1:['Arun',23,30000],2:['Amal',26,50000],3:['Anu',24,20000],4:['Kiran',27,60000]}
print(max(d.values()))
l=[]
for i in d.values():
    l.append(i[2])

print('Maximum salary : ',max(l))