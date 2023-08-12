from django.contrib import admin
from .models import StudentInfoModel, TeacherInfoModel, Customer, Staff

# Register your models here.
admin.site.register(StudentInfoModel)
admin.site.register(TeacherInfoModel)
admin.site.register(Customer)
admin.site.register(Staff)

