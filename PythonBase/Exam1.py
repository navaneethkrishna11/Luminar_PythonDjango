# 1.Answer any one of the following(5 marks)
"""
Function?Explain with example?(5 marks)
 ANS) Functions are block of code to execute a particular statement.
       There have two sides. First is to create a function that means function definition and second is to call the function.
       We use function for using the particular code repeatdly in our programs.
       There are different types of functions like built in, custom function,lambda function.
eg: def add (a,b):
      print(a+b)
    
    add(20,30)
here function is defined at beginning and called at last. so the values are passed to the function using the function call.
"""
# 2. Answer any one of the following (2 marks)
"""
a).What is Lambda Function?.Where it is used?(2 marks)
ANS) It is a inline function. Mainly used in higher order functions to solve.
     syntax => lambda args:expression
     eg: s=lambda a,b:a+b
         print(s(1,2))

"""
# 3). Answer any one of the following (3marks)
# a)Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"
i=["Python", "Is", "Great"]
for j in i:
    print(''.join(j[0]),end="")

# 4). Write a python program that takes a sentence and returns a dictionary (5 marks)
# Keys are words in the sentence.
# Values are dictionaries with:
# “length”->Length of the word
# “is_palindrome”->True if the word is palindrome,otherwise False.
# “count” ->number of occurences of the word
# Sample Input:
# Sentence=”madam and racecar are level racecar madam”
# Sample Output:
# {“madam”:{‘length’:5,’is_palindrome”:True,’count’:2},
# “and”:{‘length’:3,’is_palindrome”:False,’count’:1},
# “racecar”:{‘length’:7,’is_palindrome”:True,’count’:2},
# “are”:{‘length’:3,’is_palindrome”:False,’count’:1},
# “level”:{‘length’:5,’is_palindrome”:True,’count’:1}
# }
print()
n=input("enter the string : ")
a=n.split()
d={}
for i in a:
    l=len(i)
    is_palindrom= i == i[::-1]
    c=a.count(i)
    d[i]={'length':l,'is_palindrom':is_palindrom,'Count':c}

print(d)
# 5). Answer any one of the following
# Print the Pattern(5 marks)
"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
print()
for i in range(0,5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print()

