# # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
for i in range(1,101):
    if i%3==0 or i%5==0:
        print(i ,end=" ")
print()
#
# # # 2.Take a string input from the user and print the reverse using a for loop.(without [::-1])
n=input("enter the string : ")
rev=" "
for i in n:
    rev=i+rev
print('Reverse : ',rev)
#
# # #3.Given a number n, write a program that uses a for loop to compute the sum of its digits.
# # # Example: n = 1234 → Output: 10
n=int(input("enter the number : "))
sum=0
l=len(str(n))
for i in range(l+1):
    sum+=i
print('sum : ',sum)
#
# # # 4.Print the cumulative sum of a list.
# # # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
a=[1,2,3,4]
b=[]
sum=0
for i in a:
    sum += i
    b.append(sum)
print(b)

# # # 5.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # # Example: a = 3, b = 7 → Output: 25
a=int(input("enter first numbr : "))
b=int(input("enter the second number : "))
sum=0
for i in range(a,b+1):
    sum +=i
print('sum : ',sum)

# 6.Given a list, sum only the elements at even indices.
# Example:
#  → Sum = 10 + 30 + 50 = 90
l=[10, 20, 30, 40, 50]
i=0
sum=0
for j in l:
    if i%2==0:
        sum+=j
    i+=1
print(sum)

#7.Given a list, sum the elements until a 0 is encountered (stop at 0).
# Example: [1, 3, 5, 0, 8, 10] → Output: 9
l=[1, 3, 5, 0, 8, 10]
sum=0
for i in l:
    sum +=i
    if i == 0:
        break
print('sum : ',sum)

# 8.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
for i in range(1,1001):
    if i%7==0 and i%11==0:
        print('First number divisible by 7 and 11',i)
        break

# 9.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
l=['orange','apple','banana','kiwi']
for i in l:
    if len(i)>=5:
        print(i,end=" ")
    else :
        continue

# 10. Loop from 1 to 30 and print all numbers except those divisible by 4. Use continue.
for i in range(1,31):
    if i%4==0:
        continue
    else:
        print(i ,end=" ")
print()

# 11.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]
a =[1,2,3]
b=[]
for i in a:
    s=i**2
    b.append(s)

print('square',s)

# 12Given a string, construct a new string with all vowels removed using a loop.
s="hello world"
v='aeiouAEIOU'
n=''
for i in s:
    if i in v:
        continue
    else :
        n=n+i
print(n)

# 13.Given a list of numbers, create a new list where each number is doubled,
# but stop if any doubled number is greater than 50 (use break).
a=[3,2,1,123,4]
b=[]
for i in a:
    s=i*i
    if s>50:
        break
    else:
        b.append(s)
print('new : ',b)

# 14.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"
n=input("enter the string : ")
v="1234567890"
d=""
for i in n:
    if i in v:
        d+= i
print('new seq : ',d)

# 15.Given a list of strings, create a new list containing the length of each string.
# Input: → Output: [3, 6, 0]
n= ["cat", "banana", ""]
b=[]
for i in n:
    c=len(str(i))
    b.append(c)
print(b)

# 16.Given a list of words, create a string made of the first letter of each word.
#  → Output: "PIG"
input=["Python", "Is", "Great"]
r=""
for i in input:
    for j in i:
        r=r+j[0]
        break
print(r)


# 17.From a list of numbers, create a list where each element is the cumulative product so far.
#  → Output: [2, 6, 24]
input= [2, 3, 4]
pdt=1
b=[]
for i in input:
    pdt=pdt*i
    b.append(pdt)
print(b)

# 18.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
#  → Output: [4, 0, 2, 0]
input= [4, -3, 2, -1]
b=[]
for i in input:
    if i<0:
        b.append(0)
    else:
        b.append(i)
print('new list',b)
# 19.print the pattern
# 1
# 4 9
# 16 25 36
count=1
for i in range(1,4):
    for j in range(1,i+1):
        print(count**2,end=" ")
        count+=1
    print('')

# 20.print the pattern
#     **
#   ****
#  ******
# ********
for i in range(1,5):
    for j in range(1,5-i):
        print("",end=" ")
    for j in range(1,i+1):
        print("*"*2,end="")
    print()

