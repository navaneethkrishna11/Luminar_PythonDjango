from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from app.forms import SignupForm,LoginForm,AddSchoolData,StudentForm
from django.contrib.auth import authenticate,login,logout
from app.models import School,Student

class Home(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self):
        pass

class UserSignup(View):
    def get(self,request):
        form_instance=SignupForm()
        context = {'form': form_instance}
        return render(request,'register.html',context)
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('usrlogin')
        else:
            context = {'form': form_instance}
            return render(request, 'register.html', context)

class UserLogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username']
            p=data['password']
            user=authenticate(username=u,password=p)
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('adminhome')
            elif user :
                login(request,user)
                return redirect('studenthome')
            else:
                print('error')
                return redirect('usrlogin')
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)

class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect('home')

class StudentHome(View):
    def get(self, request):
        return render(request, "studenthome.html")


class AdminHome(View):
    def get(self, request):
        return render(request, "adminhome.html")


class AddSchool(View):
    def post(self,request):
        form_instance=AddSchoolData(request.POST)
        if form_instance.is_valid:
            form_instance.save()
            return redirect('addschool')
        context = {'form': form_instance}
        return render(request, 'addschool.html', context)
    def get(self,request):
        form_instance=AddSchoolData()
        context={'form':form_instance}
        return render(request,'addschool.html',context)

class ListSchool(View):
    def get(self,request):
        a = School.objects.all()
        context = {'school': a}
        return render(request, 'schoolist.html', context)

class DetailSchool(View):
    def get(self,request,i):
        a = School.objects.get(id=i)
        u=request.user
        can_join=True
        is_student=False
        try:
            stu=Student.objects.get(user=u)
            can_join=False
            if stu.school==a:
                is_student=True
        except:
            pass
        print(can_join,is_student)
        context = {'school': a,'can_join':can_join,'is_student':is_student}
        return render(request, 'detailview.html', context)


class StudentJoin(View):
    def get(self,request,i):
        form_instance=StudentForm()
        # a = School.objects.get(id=i)
        context = {'form': form_instance}
        return render(request, 'studentjoin.html', context)
    def post(self,request,i):
        s=School.objects.get(id=i)
        u=request.user   #current user id code
        form_instance=StudentForm(request.POST)
        if form_instance.is_valid():
            stu=form_instance.save(commit=False)
            stu.school=s
            stu.user=u
            stu.save()       #if .save() is given then it will directly save in db, but giving commit=false we can addtional data
            return redirect('listschool')

class LeaveNow(View):
    def get(self,request):
        u=request.user
        try:
            a = Student.objects.get(user=u)
            a.delete()
        except:
            pass
        return redirect('listschool')
