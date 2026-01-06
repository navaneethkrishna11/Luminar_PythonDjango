from cart.models import Cart

def countofpdt(request):
    sum = 0
    if request.user.is_authenticated:
        u=request.user
        c=Cart.objects.filter(user=u)
        for i in c:
            sum += i.quantity
    return {'count':sum}