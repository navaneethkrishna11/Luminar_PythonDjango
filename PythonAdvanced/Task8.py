# write a program to remove consecutive duplicate from a string

# delete all the repeated characters from string
a="aabccbbc"
l=[]
for i in a:
    if i not in l:
        l.append(i)
print(''.join(l))

# remove consecutive repeated characters
b="abcaabaac"
c = [a[0]]
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        c.append(a[i])
print("".join(c))

