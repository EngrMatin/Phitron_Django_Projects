from django.contrib import admin
from .models import Person, Passport

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'address')
    
@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'passport_no', 'page', 'validity')