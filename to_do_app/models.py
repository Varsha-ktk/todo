from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()

class Todo(models.Model):
      topic=models.CharField(max_length=20)
      description=models.TextField()