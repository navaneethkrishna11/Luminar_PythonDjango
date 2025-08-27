#1.write a program to find BMI(Body Mass Index)
weight = int(input("Enter the user weight in KG : "))
height2 = int(input("Enter the user height in CM : "))
height= height2/100
bmi= weight/(height**2)
if bmi<=18.4 :
    print("UNDERWEIGHT",bmi)
elif 18.5< bmi< 24.9 :
    print('NORMAL',bmi)
elif 25.0 < bmi < 39.9:
    print('OVERWEIGHT',bmi)
elif bmi>=40.0:
    print('OBESE',bmi)

#2. A toy vendor supplies three types of toys:
print('1.Battery pdt \t 2.Key pdt \t 3.Electrical pdt')
product_code= int(input("enter the code :  "))
l1=[1,2,3]
if product_code in l1:
    order_amout = int(input("enter the amount : "))
    if product_code==1:
        if order_amout >1000:
            print('Final price of product  : ',order_amout-(10*order_amout)/100)
        else:
            print('No offer! price is : ',order_amout)
    elif product_code==2:
        if order_amout>100:
            print('Final price of product : ',order_amout-(5*order_amout)/100)
        else:
            print('No offer! price is : ',order_amout)
    elif product_code==3:
        if order_amout>500:
            print('Final price of product : ', order_amout-(10 * order_amout) / 100)
        else:
            print('No offer! price is : ',order_amout)
else:
    print('Invalid code')
