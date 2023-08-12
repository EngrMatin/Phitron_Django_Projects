from django import forms
from django.core import validators
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['name', 'email', 'mobile', 'password', 'dob', 'weight', 'cgpa', 'photo']
        labels = {
            'mobile' : 'Mobile Number',
            'dob' : 'Date of birth',
            'cgpa' : 'CGPA'
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'password' : forms.PasswordInput,
            'dob' : forms.DateInput(attrs={'type':'date'}),
            'size' : forms.RadioSelect(choices = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')])
        }
        
        # validators = {
            
        #     'password' : validators.MinLengthValidator(8, message='Password must have at least 8 characters'),
        #     'email' : validators.EmailValidator(message='Enter a valid email address'),
        #     'photo' : validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        # }
        
        # required = {
        #     'dob' : False,
        #     'photo' : False,
        # }