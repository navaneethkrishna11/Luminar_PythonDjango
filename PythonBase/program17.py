i = 20
while i >= 0:
    print(i ,end=' ')
    i -= 2
print()

count=0
for i in range(200, 400):
    if i % 3 == 0 and i % 5 == 0:
        print(i,end=" ")
        count +=1
print()
print("count of number : ",count)

count=0
for i in range(1500, 2700):
    if i % 7==0:
        count +=1
print("count of number : ",count)

n=5
sum=0
while n>=0:
    sum +=n
    n -=1
print(sum)

n=5
print("sum : ",n*(n+1)/2)

n=5
sum=1
while n>0:
    sum *=n
    n -=1
print(sum)

#sum of number from (200,400)
i=200
sum=0
while i<=400:
    sum +=i
    i+=1
print('sum : ',sum)
# sum of squares of numbers from 1-10
i=1
sum=0
while(i<=10):
    sum += i**2
    i +=1
print('square : ',sum)
# sum of cubes of numbers from 1-10
i=1
sum=0
while(i<=10):
    sum += i**3
    i +=1
print('cube : ',sum)
# product of even number from 1-100
i=1
pdt=1
while(i<=100):
    if i%2 == 0:
        pdt *=i
    i +=1
print('pdt : ',pdt)
# sum and count of numbers that are divisbile by 3 in range(1,50)
i=1
sum=0
count=0
while(i<=50):
    if i%3 == 0:
        sum += i
        count +=1
    i +=1
print('sum : ',sum)
print('count : ',count)

# Factorial of a number
fact=1
n=int(input("entr a anumber : "))
while(n>0):
    fact=fact*n
    n-=1
print("fact : ",fact)

# Multiplication table
n=int(input("enter the limit : "))
i=1
while i<=10:
   print(f"{i} * {n} =",i*n)
   i+=1


n=int(input("enter the imput : "))
i=1
while(i<=n):
    if(n%i==0):
        print(i)
    i+=1

