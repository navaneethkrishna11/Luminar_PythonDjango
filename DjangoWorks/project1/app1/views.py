from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('welcome home')
#
# def index(request):
#     return HttpResponse('Welcome to index page')
#
def new(request):
    return HttpResponse('python full stack ')

context={'name':'Navaneeth Krishna','age':22}
def home(request):
    return render(request,'home.html',context)
def index(request):
    return render(request,'index.html')