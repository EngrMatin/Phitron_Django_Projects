from django import forms
from . import models

class AddBookForm(forms.ModelForm):
    class Meta:
        model = models.AddBook
        exclude = ['first_pub', 'last_pub']