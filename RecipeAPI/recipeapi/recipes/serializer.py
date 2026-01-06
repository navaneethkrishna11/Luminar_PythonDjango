from rest_framework import serializers
from .models import Recipe,Review
from django.contrib.auth.admin import User


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self,validate_data):
        user=User.objects.create_user(**validate_data) #here all the data fields area valdiated
        return user

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['recipe','rating','comment']