from django.shortcuts import render,redirect
from django.views import View
from shop.models import Product
from cart.models import Cart,Order,Order_items
from cart.forms import OrderForm
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import  method_decorator
import uuid
from django.contrib.auth.decorators import login_required

@method_decorator(login_required,name='dispatch')
class AddToCartView(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.get(user=u,product=p)
            c.quantity +=1
            c.save()
        except:
            c=Cart.objects.create(user=u,product=p,quantity=1)
            c.save()
        return redirect('cart:cartview')

class RemoveFromCart(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.get(user=u,product=p)
            if c.quantity >1:
             c.quantity -=1
             c.save()
            else:
                c.delete()
        except:
            c=Cart.objects.create(user=u,product=p,quantity=1)
            c.save()
        return redirect('cart:cartview')

class DeleteFromCart(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        u=request.user
        try:
            c=Cart.objects.get(user=u,product=p)
            c.delete()
        except:
           pass
        return redirect('cart:cartview')


class CartView(View):
    def get(self,request):
        u=request.user
        c=Cart.objects.filter(user=u)
        sum=0
        for i in c:
            sum=sum+i.subtotal()
        print('sume',sum)
        context={'cart':c,'subtotal':sum}
        return render(request,'cart.html',context)

class Checkout(View):
    def post(self,request):
        form_instance=OrderForm(request.POST)
        if form_instance.is_valid():
            o=form_instance.save(commit=False)
            o.user=request.user
            c = Cart.objects.filter(user=request.user)
            sum = 0
            for i in c:
                sum = sum + i.subtotal()
            o.amount=sum
            o.save()
            if o.payment_method == 'online':
                # create a connection with razorpay
                client=razorpay.Client(auth=("rzp_test_Rn84s7DWfozvRl","vjpKToTkIK2uPtlBJ5UX327B"))
                # creates a order in razorpay
                response_payment=client.order.create({'amount':(o.amount*100),'currency':'INR'})
                # retrives the order id from response_payment
                id=response_payment['id']
                # saves it in order table
                o.order_id=id
                o.save()
                context={'payment':response_payment}
                return render(request, 'payment.html', context)
            else:
                id='ORD_COD' + uuid.uuid4().hex[:14]
                o.order_id=id
                o.is_ordered=True
                o.save()
                for i in c:
                    item=Order_items.objects.create(order_id=o,product=i.product,quantity=i.quantity)
                    item.save()
                    item.product.stock -= item.quantity
                    item.product.save()
                c.delete()
                return render(request,'payment.html')


    def get(self,request):
        form_instance=OrderForm()
        context={'form':form_instance}
        return render(request,'checkout.html',context)

@method_decorator(csrf_exempt,name='dispatch') #to avoid csrf error from razorpay
class PaymentSuccess(View):
    def post(self,request):
        # print(request.user.username)
        re=request.POST
        id=re['razorpay_order_id'] #read the order id from the razorpay response
        o=Order.objects.get(order_id=id)
        o.is_ordered=True #set is_ordered status to True
        o.save()

        u=request.user
        c=Cart.objects.filter(user=u)
        for i in c:
            item=Order_items.objects.create(order_id=o,product=i.product,quantity=i.quantity)
            item.save()
            item.product.stock -= item.quantity
            item.product.save()

        # cart delete
        c.delete()
        return render(request,'payment_success.html')

class MyOrder(View):
    def get(self,request):
        u=request.user
        o=Order.objects.filter(user=u,is_ordered=True)
        context={'orders':o}
        return render(request,'myorders.html',context)