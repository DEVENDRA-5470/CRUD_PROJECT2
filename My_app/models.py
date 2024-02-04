from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    idno = models.CharField(max_length=20, unique=True)
    img=models.ImageField(blank=True,upload_to='uploads/')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rollno = models.IntegerField()
    class_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name