# Perfect number finding program
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum +=i

    if sum == n:
        print('perfect number')
    else:
        print('not perfect')

perfect(6)

# define a fun to convert celsius to farnheit
def conv(n):
    f=(n*9/5)+32
    print("fareheiet",f)

conv(130)