n=int(input("enter the number : "))
if n<=1:
    print('co prime')
else:
    for i in range(2,n):
        if n%i == 0:
            print('no prime')
            break
    else :
        print('prime')

for i in range(1,5):
    for j in range(1,4):
        print(i,j,end=" ")
    print()

print()
for i in range(1,4):
    print('hello '*3)

for i in range(1,5):
    for j in range(1,4):
        print(i*j,end=" ")
    print()
print()


