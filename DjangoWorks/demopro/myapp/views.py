from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('First Page')

def second(request):
    return HttpResponse('Second Page')