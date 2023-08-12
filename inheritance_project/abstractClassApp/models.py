from django.db import models

# Create your models here.
class CommonInfoClass(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=30)
    
class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()
    

        
class ContactInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=30)
    class Meta:
        abstract = True

class Customer(ContactInfo):
	phone = models.CharField(max_length=15)

class Staff(ContactInfo):
	position = models.CharField(max_length=10)