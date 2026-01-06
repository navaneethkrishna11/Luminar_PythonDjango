from django.db import models

class Book(models.Model):
    image=models.ImageField(upload_to='images')
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    language = models.CharField(max_length=20)
    price = models.IntegerField()
    page = models.IntegerField()

