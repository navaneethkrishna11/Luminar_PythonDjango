from django import forms

# class Addbook(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language=forms.CharField()
#
from books.models import Book     # defines form based on model
class Addbook(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
