from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=30)
    price=models.IntegerField()
    page=models.IntegerField()
    language=models.CharField(max_length=20)

