from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete=models.CASCADE)
    passport_no = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()

