from django import forms

class Additionform(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class Factorialform(forms.Form):
    num=forms.IntegerField()

class Bmiform(forms.Form):
    weight=forms.IntegerField()
    height=forms.IntegerField()

class Signupform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.CharField()
    phone=forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea)
    genderchoices=(('male','Male'),('female','Female'))
    gender=forms.ChoiceField(choices=genderchoices,widget=forms.RadioSelect)
    rolechoices=(('admin','Admin'),('student','Student'))
    role=forms.ChoiceField(choices=rolechoices)
