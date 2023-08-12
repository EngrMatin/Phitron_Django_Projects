from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.StudentInfo)
@admin.register(models.ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    
@admin.register(models.ReviewInfo)
class ReviewInfoAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'review')