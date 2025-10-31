from django.db import models


class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    designtaion=models.CharField(max_length=20)
    email=models.CharField(max_length=20)

