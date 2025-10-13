#Given a dictionary
employee={
    "id":101,
    "name":"Anjali",
    "department":"HR",
    "salary":450000
}

#Print the department of employee
print("Employee :",employee["department"])
#Updates the salary to 50000
employee["salary"]=50000
#print the updated salary
print("Updated salary : ",employee["salary"])
#Add a new key -value pair location:Bangalore to employee
employee['location']='Bangalore'

#Given a string
msg="Hello, Python World!"
#print the first character
print("First character : ",msg[0])
#print the last character
print("Last character : ",msg[-1])
#print the first 5 characters
print("First five characters : ",msg[:5])
#print the reverse
print("Reverse : ",msg[::-1])
#print the length
print("Length : ",len(msg))



#Given a set
s={'dog','cat','rabbit','cow'}
#add a new animal "lion" to set
s.add('lion')
#print the updated set
print("Updated set : ",s)


#Given a list
l=['Riya',"Ankit","Sara","Manu"]
#Print the first student
print("First student : ",l[0])
#Changes the second value to Amit
l[1]='Amit'
#Add a new student Amal
l.append('Amal')
#Print the length
print("length",len(l))
#print the updated list
print("Updated list : ",l)

#5 key features of Python
"""
> High level language
> Interpretar is used for running python code
> Machine independent
> Portable
> Dynamically values assigned 
> Easy to use
"""
#What is the difference between mutable and immutable type?Give example
"""
Mutable means in that we can update characters or values.
eg: list , set, dictonary

Imutable means in that we can not update characters or values.
eg: string,tuple
"""
#What are the Major datatypes in Python?
"""
Numerical types, String types, Mapping type, Boolean type
"""
