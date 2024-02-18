from django.forms import ModelForm, TextInput
from django import forms
from .models import User

class signUpForm(ModelForm):
    password_1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}), required=False)
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'form-control'}), required=False)

    class Meta:
        model = User
        fields = [
            "user_name",
            "email", 
        ]

        widgets = {
            'user_name': TextInput(attrs={'placeholder': 'User Name', 'class':'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Enter Email', 'class':'form-control'}),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email is None or email.strip() == '':
            raise forms.ValidationError("The email cannot remain empty")
        
        return email
    
    def clean_user_name(self):
        user_name =  self.cleaned_data.get('user_name')

        if user_name is None or user_name.strip() == '':
            raise forms.ValidationError("The user name cannot remain empty")
        return user_name
  
    def clean_password_1(self):
        password_1 = self.cleaned_data.get("password_1")

        if password_1 is None or password_1.strip() == '':
            raise forms.ValidationError("The password cannot remain empty")
        
        if len(password_1) < 6:
            raise forms.ValidationError("The password cannot be less than 6 characters")
        
        return password_1
    
    def clean_password_2(self):
        password_2 = self.cleaned_data.get("password_2")

        if password_2 is None or password_2.strip() == '':
            raise forms.ValidationError("The password cannot remain empty")
        
        return password_2
    
    def clean(self):
        cleaned_data = super().clean()
        password_1 = cleaned_data.get("password_1")
        password_2 = cleaned_data.get("password_2")

        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data