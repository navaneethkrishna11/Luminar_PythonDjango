from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    duedate = models.CharField(max_length=20)


