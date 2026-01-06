from django.shortcuts import render,redirect
from django.views import View
from shop.models import Category,Product
from shop.forms import RegisterForm,LoginForm,CategoryForm,ProductForm
from django.contrib.auth import logout,authenticate,login
from django.utils.decorators import  method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def admin_required(fun):
    def wrapper(request):
        if not request.user.is_superuser:
            return HttpResponse('not allwd')
        else:
           return fun(request)
    return wrapper

class CategoryView(View):
    def get(self,request):
        b=Category.objects.all()
        context={'category':b}
        return render(request,'categories.html',context)

class MoreView(View):
    def get(self, request,i):
        b=Category.objects.get(id=i)
        c=Product.objects.filter(category=b)
        context = {'more': c,'category':b}
        return render(request, 'details.html',context)

class ProductDetailView(View):
    def get(self,request,i):
        b=Product.objects.get(id=i)
        context={'products':b}
        return render(request,'productdetails.html',context)

class LoginView(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            u = data['username']
            p = data['password']
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
                return render(request,'categories.html')
            else:
                print('failed')
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)

class RegisterView(View):
    def get(self,request):
        form_instance=RegisterForm()
        context={'form':form_instance}
        return render(request,'register.html',context)
    def post(self,request):
        form_instance=RegisterForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:usrlogin')
        else:
            context = {'form': form_instance}
            return render(request, 'register.html', context)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('shop:usrlogin')

# @method_decorator(login_required,name='dispatch')
@method_decorator(admin_required, name='dispatch')
class AddCategoryView(View):
    def get(self, request):
        form_instance = CategoryForm()
        context = {'form': form_instance}
        return render(request, 'addcategories.html', context)
    def post(self, request):
        form_instance = CategoryForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request, 'addcategories.html')

@method_decorator(login_required,name='dispatch')
class AddProductsView(View):
    def get(self, request):
        form_instance = ProductForm()
        context = {'form': form_instance}
        return render(request, 'addproducts.html', context)
    def post(self, request):
        form_instance = ProductForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request, 'addproducts.html')

