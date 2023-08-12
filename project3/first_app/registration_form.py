from django import forms
from django.core import validators

class RegistrationForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=30, widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))
    mobile = forms.CharField(label='Mobile Number')
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email address')])
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(8, message='Password must have at least 8 characters')])
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type':'date'}), required=False)
    weight = forms.IntegerField(min_value=20, max_value=100)
    cgpa = forms.DecimalField(label='CGPA', min_value=0, max_value=4, max_digits=3, decimal_places=2)
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}), required=False)
    size = forms.ChoiceField(widget=forms.RadioSelect, choices = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')])
    pizza = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')])
    review = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':31}), initial='Very nice!', disabled=True)
    youtube = forms.BooleanField(label='Have you subscribed the youtube channel?', required=False)
    file = forms.FileField(help_text='Submit PP size photo, file size less than 50kb', validators=[validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def clean(self):
        cleaned_data = super().clean()
        mail = self.cleaned_data['email']
        pw = self.cleaned_data['password']
        con_pw = self.cleaned_data['confirm_password']
        if ('@' not in mail) or ('.' not in mail):
            raise forms.ValidationError('Please enter a valid email ID')
        if pw != con_pw:
            raise forms.ValidationError('Passwords do not match!')