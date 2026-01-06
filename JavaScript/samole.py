ar = [3, 2, 5, 2, 1]
target = 9
d = {}

for i, num in enumerate(ar):
    c = target - num
    if c in d:
        print(d[c], i)
        break
    d[num] = i

from collections import defaultdict
counter=defaultdict(int)
s='hellooo'
for i in s:
    counter[i] += 1

print(counter)
