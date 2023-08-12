from django.contrib import admin
from .models import AddBook

# Register your models here.
# admin.site.register(BookStoreModel)
class AddBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category', 'first_pub', 'last_pub')
admin.site.register(AddBook, AddBookAdmin)