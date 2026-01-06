from django.db import models
from rest_framework.authtoken.admin import User
from django.core.validators import MinValueValidator,MaxValueValidator
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=30)
    instructions=models.TextField()
    ingredients=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    mealtype=models.CharField(max_length=20)
    cusine=models.CharField(max_length=20)

class Review(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


