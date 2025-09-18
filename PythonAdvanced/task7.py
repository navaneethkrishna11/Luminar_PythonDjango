# Daily Task 7
for i in range(1,6):
    for j in range(0,i):
        a=i+j
        if a%2!=0:
            print("1",end=' ')
        else:
            print("0",end=" ")
    print("")

class Company:
    def show(self):
        print("luminar")
class Deploy(Company):
    def show(self):
        super().show()
        print("Website Deployed in Vercel")
class Testing(Company):
    def show(self):
        super().show()
        print("Testing on Selenium")
class Product(Deploy,Testing):
    def output(self):
        super().show()
        print('Product released!')

p=Product()
p.output()