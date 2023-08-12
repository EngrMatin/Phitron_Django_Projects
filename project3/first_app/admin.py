from django.contrib import admin
from .models import Student
# from . import models

# Register your models here.
# admin.site.register(models.Student)

class Student_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email', 'password', 'confirm_password', 'dob', 'weight', 'size', 'cgpa', 'review', 'youtube', 'photo')
admin.site.register(Student, Student_admin)
