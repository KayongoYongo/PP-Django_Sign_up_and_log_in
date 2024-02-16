from django.forms import ModelForm, TextInput
from django.core.validators import MinLengthValidator
from django import forms
from .models import User

class UserForm(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), required=False)

    class Meta:
        model = User
        fields = [
            "user_name",
            "email", 
        ]

        widgets = {
            'user_name': TextInput(attrs={'placeholder': 'User Name'}),
            'email': TextInput(attrs={'placeholder': 'Enter Email'}),
            'password': TextInput(attrs={'placeholder': 'Password'}),
        }

        labels = {
            "user_name": '',
            "email": '', 
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        # Adding a validator to enforce minimum password length
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email is None or email.strip() == '':
            raise forms.ValidationError("The email cannot remain empty")
        return email
    
    def clean_user_name(self):
        user_name =  self.cleaned_data.get('user_name')

        if user_name is None or user_name.strip() == '':
            raise forms.ValidationError("The user name cannot remian empty")
        return user_name
    
    
    def clean_password(self):
        password1 = self.cleaned_data.get("password1")

        if password1 is None or password1.strip() == '':
            raise forms.ValidationError("The password cannot remian empty")
        
        if len(password1) < 6:
            raise forms.ValidationError("The password cannot be less than 6 characters")
        
        return password1