from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    dob = models.DateField()
    weight = models.IntegerField()
    size = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    review = models.TextField(max_length=100)
    youtube = models.BooleanField()
    photo = models.FileField()
    
    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Mobile: {self.mobile}'