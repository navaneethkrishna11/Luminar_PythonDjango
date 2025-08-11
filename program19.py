# l=[11,23,56,34]
# sum=0
# for i in l:
#     sum +=i
# print(sum)
#
# for i in range(100,1000):
#     print(i ,end=' ')
# print()
#
# colors=['red','green','blue','black','orange']
# for i in colors:
#     if "b" in i[0]:
#         print(i ,end=" ")
# print()
#
# f=1234
# for i in str(f):
#     print(i)
# n=1234
# a=n
# sum=0
# while a>0:
#     digit = a%10
#     sum +=digit
#     a //=10
# print(sum)
#
#
# n=int(input("enter the number  : "))
# a=str(n)
# l=len(str(n))
# sum=0
# for i in a:
#     sum += int(i)**l
#
# if sum == n:
#     print('armstrong')
# else:
#     print('not')

n=1234
s=str(n)
rev=" "
for i in s:
    rev= i + rev
print(rev)

n=1234
sum=0
while n>0:
    digits = n%10
    sum = sum * 10 +digits
    n //=10
print(sum)

