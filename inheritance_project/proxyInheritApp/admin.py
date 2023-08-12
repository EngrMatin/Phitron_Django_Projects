from django.contrib import admin
from .models import FriendModel, MeModel, Person, Employee, Manager

# Register your models here.

@admin.register(FriendModel)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'section', 'attendance', 'cw', 'hw')

@admin.register(MeModel)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'section', 'attendance', 'cw', 'hw')
    
@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    
@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'job_title', 'salary')
    
@admin.register(Manager)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'job_title', 'salary')

