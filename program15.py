#nested if porgram for +ve even,+ve odd , -ve even, -ve odd
i=int(input("enter the value : "))
if(i>0):
    if(i%2==0):
        print("positive even")
    else:
        print('negative even')
else:
    if(i%2==0):
        print('negative even')
    else:
        print('negative odd')

# nested if example program for a shopkeeper
while True:
    # battery=1
    # key=2
    # electrical=3
    print('1.Battery pdt \t 2.Key pdt \t 3.Electrical pdt')
    product_code= int(input("enter the code :  "))
    order_amout= int(input("enter the amount : "))

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




