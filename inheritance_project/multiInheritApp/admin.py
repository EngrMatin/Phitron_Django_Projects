from django.contrib import admin
from .models import EmployeeModel, ManagerModel, Person, Teacher, Student

# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'city')
admin.site.register(EmployeeModel, EmployeeModelAdmin)

@admin.register(ManagerModel)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'city', 'take_interview', 'hiring')
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'address')
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'address', 'designation', 'salary')
    

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'address', 'roll', 'tution_fee')
admin.site.register(Student, StudentAdmin)