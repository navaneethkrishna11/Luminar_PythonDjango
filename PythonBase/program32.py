#Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
#sum of positive even numbers
pe=sum([i for i in l if i>0 and i%2==0 ])
print('positive even method 1 : ',sum(list(filter(lambda x:x>0 and x%2==0,l))))
print('positive even method 2 :' ,pe)
#sum of positive odd numbers
po=sum([i for i in l if i>0 and i%2!=0 ])
print('positive odd :' ,po)
#sum of  negative even numbers
ne=sum([i for i in l if i<0 and i%2==0 ])
print('negative even :' ,ne)
#sum of negative odd numbers
no=sum([i for i in l if i<0 and i%2!=0 ])
print('negative odd :' ,no)
#count of positive numbers
a=len([i for i in l if i>0])
print('count of positive : ',a)
print('count of positive method 1 : ',len(list(filter(lambda x:x>0,l))))
#count of negative numbers
print('count of negative : ',len([i for i in l if i<0]))
#Given a list
l=['python','coding','is','easy','and','fun']
print(" ".join(l))
