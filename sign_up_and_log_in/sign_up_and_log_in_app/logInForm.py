from django import forms
from django.forms import ModelForm
from .models import User

class logInForm(ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email is None or email.strip() == '':
            raise forms.ValidationError("The email cannot remain empty")
        
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get("password")

        if password is None or password.strip() == '':
            raise forms.ValidationError("The password cannot remain empty")
        
        return password