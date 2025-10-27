from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    if request.method=='GET':
        return render(request,'addition.html')
    if request.method == 'POST':
         print(request.POST)
         n1=request.POST['num1']
         n2=request.POST['num2']
         sum=int(n1)+int(n2)
         context={'result':sum}
         return render(request, 'addition.html',context)

def fact(request):
    if request.method=='GET':
        return render(request,'fact.html')
    if request.method=='POST':
        n1=request.POST['num1']
        fact=1
        for i in range(1,int(n1)+1):
            fact=fact*i

        context={'result':fact}
        return render(request,'fact.html',context)

def bmi(request):
    if request.method=='GET':
        return render(request,'bmi.html')
    if request.method=='POST':
        n1=request.POST['weight']
        n2=request.POST['height']
        sol=int(n1)/(int(n2)/100)**2
        context={'result':sol}
        return render(request,'bmi.html',context)

