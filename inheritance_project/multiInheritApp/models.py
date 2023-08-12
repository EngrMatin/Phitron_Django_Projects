from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=64)
    mobile = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

class Teacher(Person):
    designation = models.CharField(max_length=30)
    salary = models.IntegerField()

class Student(Person):
    roll = models.CharField(max_length=20)
    tution_fee = models.CharField(max_length=20)
