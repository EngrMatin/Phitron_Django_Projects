from django.db import models

# Create your models here.
class AddBook(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices={('Mystery','Mystery'), ('Thriller','Thriller'), ('Humor','Humor'), ('Horror','Horror'), ('Sci-Fi','Sci-Fi'), ('Novel','Novel'), ('Computer Science','Computer Science'), ('Drama','Drama'), ('Comedy','Comedy'), ('Religious','Religious'), ('Adventure','Adventure'), ('Poetry','Poetry') })
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'Name: {self.book_name}, Author: {self.author}'