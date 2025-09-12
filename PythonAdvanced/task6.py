# 1
# 22
# *
# 4444
# 55555
# **
count = 0
for i in range(1,7):
    for j in range(0,i):
        if i%3==0:
            count += 1
            print("*" * count,end="")
            break
        else:
            print(i, end='')
    print("")

for i in range(1,7):
    if i % 3 == 0:
        count = i // 3
        print("*" * count, end="")
    else:
        for j in range(0,i):
            print(i, end='')
    print("")

