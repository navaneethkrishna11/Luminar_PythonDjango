class Category:
    def __init__(self):
        self.showcategoryname='alliazn'
    def show_category_info(self):
        print("category info:",self.showcategoryname)

class Product(Category):
    def __init__(self):
        super().__init__()
        self.prodcutname=input("enter the prodcut name : ")
        self.price=int(input("enter the price : "))
        self.quantity=int(input("enter the quantity : "))
    def show_product_info(self):
        print(self.prodcutname,self.price,self.quantity)
    def total_price(self):
        print('total price = ',self.quantity*self.price)

p=Product()
p.show_category_info()
p.show_product_info()
p.total_price()


