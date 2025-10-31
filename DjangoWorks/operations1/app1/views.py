from django.shortcuts import render
from django.views import View
from app1.forms import Additionform, Factorialform, Bmiform, Signupform

class Home(View):
    def get(self, request):
        return render(request,'home.html')

class Addition(View):
    def get(self, request):
        form_instance = Additionform()
        context = {'form': form_instance}
        return render(request, 'addition.html', context)

    def post(self, request):
        form_instance = Additionform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            n1 = data['num1']
            n2 = data['num2']
            sum_result = int(n1) + int(n2)
            context = {'result': sum_result, 'form': form_instance}
        return render(request, 'addition.html', context)

class Factorial(View):
    def get(self, request):
        form_instance = Factorialform()
        context = {'form': form_instance}
        return render(request, 'fact.html', context)

    def post(self, request):
        form_instance = Factorialform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            n1 = int(data['num'])
            fact = 1
            for i in range(1, n1 + 1):
                fact *= i
            context = {'result': fact, 'form': form_instance}
        return render(request, 'fact.html', context)

class Bmi(View):
    def get(self, request):
        form_instance = Bmiform()
        context = {'form': form_instance}
        return render(request, 'bmi.html', context)

    def post(self, request):
        form_instance = Bmiform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            weight = float(data['weight'])
            height = float(data['height'])
            bmi_result = weight / ((height / 100) ** 2)
            context = {'result': bmi_result, 'form': form_instance}
        return render(request, 'bmi.html', context)

class SignupView(View):
    def get(self,request):
        form_instance= Signupform()
        context = {'form': form_instance}
        return render(request, 'register.html', context)
    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)

        return render(request,'register.html')


