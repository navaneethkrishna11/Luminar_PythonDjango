# Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5 but not both
for i in range(1,101):
    if (i%3==0 or i%5==0) and not (i%3==0 and i%5==0):
        print(i)
