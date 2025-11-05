from django.shortcuts import render
from django.views import View
from movieapp.forms import MovieForm
from movieapp.models import Movie
class Home(View):
    def get(self,request):
        m=Movie.objects.all()
        context={'movie':m}
        return render(request,'home.html',context)

class Addmovie(View):
    def post(self,request):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return render(request,'addmovie.html')
    def get(self,request):
        form_instance=MovieForm()
        context={'form':form_instance}
        return render(request,'addmovie.html',context)


