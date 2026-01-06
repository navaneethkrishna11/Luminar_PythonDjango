from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self,validate_data):
        user=User.objects.create_user(**validate_data) #here all the data fields area valdiated
        return user
