from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

context={'name':'Navaneeth Krishna','age':22}
def home(request):
    return render(request,'home.html',context)

def viewbooks(request):
    return render(request,'viewbooks.html')


def addbook(request):
    return render(request,'addbooks.html')