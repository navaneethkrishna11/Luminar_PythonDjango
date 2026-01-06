from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import School,Student

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']
    def _init_(self):
        super()._init_()
        for field in self.fields.values():
            field.help_text = None


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class AddSchoolData(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','place']