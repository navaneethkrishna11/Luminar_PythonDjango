from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from app1.forms import SignupForm,LoginForm
from django.core.mail import send_mail

from django.contrib.auth import authenticate,login,logout
class Home(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self):
        pass

class UserSignup(View):
    def get(self,request):
        form_instance=SignupForm()
        context = {'form': form_instance}
        return render(request,'signup.html',context)
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()
            send_mail(
                "Django Auth OTP",
                u.otp,
                "navaneet011@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('verify')
        else:
            context = {'form': form_instance}
            return render(request, 'signup.html', context)

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
            elif user and user.role == 'student':
                login(request,user)
                return redirect('studenthome')
            elif user and user.role == 'teacher':
                login(request,user)
                return redirect('teacherhome')
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
        return redirect('usrlogin')

class StudentHome(View):
    def get(self, request):
        return render(request, "studenthome.html")


class TeacherHome(View):
    def get(self, request):
        return render(request, "teacherhome.html")

from app1.models import CustomUser
class OtpVerify(View):
    def post(self,request):
        o=request.POST['o']
        u=CustomUser.objects.get(otp=o)
        u.is_active=True
        u.is_verified=True
        u.otp=None
        u.save()
        return redirect('usrlogin')
    def get(self,request):
        return render(request,'verify.html')

