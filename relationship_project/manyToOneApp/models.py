from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    caption = models.CharField(max_length=50)
    details = models.CharField(max_length=255)
