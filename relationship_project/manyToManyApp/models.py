from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name='teachers')
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    
    def studentList(self):
        return ', '.join([str(i) for i in self.student.all()])
    
    def __str__(self):
        return self.name