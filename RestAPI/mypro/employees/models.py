from django.db import models

class Employee(models.Model):
    employee_id=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)

