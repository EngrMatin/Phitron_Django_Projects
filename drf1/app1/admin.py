from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.StudentInfo)
@admin.register(models.StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll')
    
@admin.register(models.CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'student', 'course_name', 'marks')