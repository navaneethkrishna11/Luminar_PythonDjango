from django.shortcuts import render, redirect
from django.views import View
from app.models import Task
from app.forms import AddTask

class Home(View):
    def get(self, request):
        tasks = Task.objects.all()
        form = AddTask()
        context = {'tasks': tasks, 'form': form}
        return render(request, 'home.html', context)

    def post(self, request):
        form = AddTask(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

class EditTask(View):
    def get(self, request, i):
        task = Task.objects.get(id=i)
        form = AddTask(instance=task)
        context={'form':form}
        return render(request, 'edit.html', context)

    def post(self, request, i):
        task = Task.objects.get(id=i)
        form = AddTask(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')


class DeleteTask(View):
    def get(self, request, i):
        Task.objects.get(id=i).delete()
        return redirect('home')
