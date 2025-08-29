 # Given a list of integers, create a new list where all negative numbers are replaced with 0.
# Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
a=[4,-3,2,-1]
b=[]
for i in a:
    if int(i)<0:
        i=0
        b.append(i)
    else:
        b.append(i)
print('New Pattern : ',b)

# Print pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()
for i in range(1,5):
    for j in range(1,j):
        print(j,end=" ")
    print()