from django.contrib import admin
from .models import AddBook

# Register your models here.
# admin.site.register(BookStoreModel)
class AddBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'isbn', 'first_pub', 'last_pub', 'no_of_books')
admin.site.register(AddBook, AddBookAdmin)