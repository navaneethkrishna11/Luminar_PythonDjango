from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Register(View):
    def get(self,request):
        return render(request,'register.html')

class Login(View):
    def get(self,request):
        return render(request,'login.html')



