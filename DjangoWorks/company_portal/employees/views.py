from django.shortcuts import render
from django.views import View
from employees.forms import Addemploye
from employees.models import Employee

class AddEmployees(View):
    def get(self,request):
        form_instance=Addemploye()
        context = {'form': form_instance}
        return render(request,'addemployees.html',context)
    def post(self,request):
        form_instance=Addemploye(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return render(request,'addemployees.html')
