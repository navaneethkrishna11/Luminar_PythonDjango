dict={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
n='223'
for i in n:
    print(dict[i],end=" ")
print('')
r = {}
for i in n:
    if i in dict:
        r[i] = dict[i]
print('result in dict : ',r)


a=12
b=10
