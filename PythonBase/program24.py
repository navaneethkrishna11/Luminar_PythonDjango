# # l=[['is','am','are'],['was','were']]
# # for i in l:
# #     for j in i:
# #         print(j ,end=" ")
# #     print()
# #
# # d={1:['dog','cat','sheep'],2:['tiger','lion','bear']}
# # for i in d.values():
# #     for j in i :
# #         print(j ,end=" ")
# # print()
# # l=['apple','orange','pineapple']
# # for i in l:
# #     for j in i :
# #         print(j)
#
# l=[3,2,1,64,3]
# new=[i**2 for i in l]
# print(new)
#
# l=['apple','orange','pineapple']
# new=[i[0] for i in l]
# print(new)
#
# l=[12,75,67,13,56]
# new=[i for i in l if i%2==0]
# print(new)
# new1=[i for i in l if i%2!=0]
# print(new1)
# new2=[i for i in l if i<50]
# print(new2)
#
# #Given a list
# fruits=['apple','banana','orange','pineapple','avocado']
# #create a new list with elements whose length >5
# f=[i for i in fruits if len(i)>5]
# print('Fruit Length : ',f)
# ##Given a list
# l=[12,39,'hello',8.7,-98,-11,5,'python']
# #create a new list with only string vvalues
# new=[i for i in l if type(i)==str]
# print('string : ',new)
# #create a new list with only positive values
# pos=[i for i in l if type(i)==int or type(i) == float if i>0]
# print('positive value : ',pos)
# #create a new list with float values
# f=[i for i in l if type(i)==float]
# print('float : ',f)
# #create a list with elements whose value is divisible by 3 in the range (1,100)
# a=[i for i in range(1,101) if i%3==0]
# print('Divisble by 3 : ',a)
# #Given a string
# s="python programming"
# s1=[i for i in s if i in 'aeiouAEIOU']
# print('vowels : ',s1)
# #given a dictionary
# d={101:'Arun',102:'Amal',103:'Anu'}
# m=[i for i in d.values()]
# print('values : ',m)
# d={'a':10,'b':15,'c':20,'d':25}
# e=[i for i in d.values() if i%2==0]
# print('even values : ',e)

s='hello world'
new={i for i in s if i!=" "}
print(new)

d={1:1,2:4,3:6,4:2}
new={i:i*2 for i in d}
print(new)

s="python is a programming lanugage"
new={i:len(i) for i in s.split()}
print(new)

l=[1,1,1,2,4,4,4,2,6,5,9]
n=list(set(l))
print(n)

l=[1,1,1,2,4,4,4,2,6,5,9]
new=[]
new=[new.append(i) or i for i in l if i not in new]
print(new)

l=[10,20,30,40]
a={i:i for i in l}
print("dict : ",a)

l=[10,20,30,40]
a={i:l[i] for i in range(len((l)))}
print("dict : ",a)