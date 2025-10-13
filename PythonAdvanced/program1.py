f=open("k.txt",'r')
s=f.read()
print(s) #read all data from file
pa=f.readlines()
print(pa) #read in list format
"""
read() : read all the lines 
read(size) : read that much number of characters
readlines(size) :  read complete data in list format
readline () : read single lines from a file
"""

# write a program to find number of lines in a file
# f=open("a.txt","r")
# s=f.readlines()
# print('len : ',len(s))
# print(s)
# write a program to find number of words in a file
# q=f.read()
# print('len of words : ',len(q.split()))

# f=open("b.txt","w")
# a="""
# Although still only the fourth most widely used JavaScript framework,
# Svelte has consistently been the most admired by developers in recent years,
# thanks to its elegant API and its creators’ discipline in saying “no”
# to clutter.In this month’s featured article, Senior Developer
# Facundo Corradini breaks down Svelte 5’s new Runes-based reactivity
# and other upgrades that make Svelte smaller, faster, and more explicit.
# """
# f.write(a)

# write a program to find a word in file
# f=open("b.txt","r")
# a=input("enter : ")
# s=f.read()
# if a in s.split():
#     print("present")
# else:
#     print("not")

# print last 5 lines from a file
# f = open("b.txt", "r")
# lines = f.readlines()
# for line in lines[-5:]:
#     print(line, end="")

# write a program to print find the number of letter,digits and spaces
# f = open("b.txt", "r")
# s=f.read()
# a_count=0
# d_count=0
# s_space=0
# for i in s:
#     if i.isalpha():
#         a_count+=1
#     elif i.isdigit():
#         d_count+=1
#     elif i.isspace():
#         s_space+=1
# print(a_count,d_count,s_space)

# write a line to the file
f = open("b.txt", "r")
s=f.readlines()
s[1]="Line2 is changed \n"
f=open("b.txt","w")
f.writelines(s)


