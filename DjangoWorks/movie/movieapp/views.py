from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def addmovie(request):
    return render(request,'addmovie.html')
