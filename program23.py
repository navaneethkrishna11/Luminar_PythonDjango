l=['kelly','emy','alen']
le=len(l)
for i in l:
    for j in range(le):
        print(i ,end=' ')
    print(" ")
print()

for i in range(1,4):
    print(i)
    for j in range(1,4):
      print(j,end=" ")
    print()

print()

for i in range(1,5):
    for j in range(0,i):
        print("*",end=" ")
    print()
print()

for i in range(1,5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

print()
for i in range(2,9,2):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

for i in range(1,9,2):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

for i in range(1,5):
    for j in range(1,i+1):
        if j%2==0:
            print(2 ,end=" ")
        else:
            print(1 ,end=" ")
    print()

print()
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print(i ,end=" ")
        else:
            print(0 , end=" ")
    print()

print()
count=1
for i in range(1,5):
    for j in range(1,i+1):
        print(count ,end=" ")
        count+=1
    print()

print()
k=65
for i in range(1,5):
    for j in range(0,i):
        print(chr(k),end=" ")
    k=k+1
    print()

print()
k=65
for i in range(1,5):
    for j in range(0,i):
        print(chr(k),end=" ")
        k+=1
    print()
print()

print()
for i in range(1,5):
    k = 65
    for j in range(0,i):
        print(chr(k),end=" ")
        k=k+1

    print()

print()
for i in range(1,8):
    for j in range(i,8):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

print()
k=3*2
for i in range(1,5):
    for j in range(1,k+1):
        print(end=" ")
    k=k-2
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(1,6):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(i,6):
        print("*",end=" ")
    print()


for i in range(1,5):
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(2,5):
    for j in range(i,5):
        print("*",end=" ")
    print()

print()
for i in range(1,6):
    for j in range(i,6):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(2,6):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(i,6):
        print("*",end=" ")
    print()

print()
for i in range(1,6):
    for j in range(i,6):
        print(" ",end="")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(2,6):
    for j in range(0,i):
        print(" ",end="")
    for j in range(i,6):
        print("*",end=" ")
    print()










