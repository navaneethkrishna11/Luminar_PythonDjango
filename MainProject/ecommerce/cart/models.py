from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    def subtotal(self):
        return self.product.price*self.quantity

class Order(models.Model):
    order_id=models.CharField(max_length=20,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.IntegerField()
    address=models.TextField(max_length=30)
    phone=models.IntegerField()
    payment_method=models.CharField(max_length=30)
    ordered_Date=models.DateTimeField(auto_now_add=True)
    is_ordered=models.BooleanField(default=False)
    delivery_status=models.CharField(default='pending',max_length=20)

class Order_items(models.Model):
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='products')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()





