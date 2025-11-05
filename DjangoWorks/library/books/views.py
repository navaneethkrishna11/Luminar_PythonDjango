from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from books.forms import Addbook
from books.models import Book
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class ViewBooks(View):
    def get(self,request):
        b=Book.objects.all()
        context={'books':b}
        return render(request, 'viewbooks.html',context)

class AddBooks(View):
    def get(self,request):
        form_instance=Addbook()
        context = {'form': form_instance}
        return render(request,'addbooks.html',context)
    def post(self,request):
        form_instance=Addbook(request.POST,request.FILES)
        if form_instance.is_valid():
            # data=form_instance.cleaned_data
            # print(data)
            # t = data['title']
            # a = data['author']
            # p = data['price']
            # pg = data['pages']
            # l = data['language']
            # b=Book.objects.create(title=t,author=a,price=p,page=pg,language=l)
            # b.save()
            form_instance.save()
            return render(request,'addbooks.html')

class EditView(View):
    def get(self,request):
        return render(request,'edit.html')
class DetailsView(View):
    def get(self, request):
        return render(request, 'details.html')

class Delete(View):
    pass