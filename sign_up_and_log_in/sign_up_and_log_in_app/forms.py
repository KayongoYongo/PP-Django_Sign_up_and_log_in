from django.forms import ModelForm, TextInput
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "second_name",
            "email", 
            "phone_number", 
            "hashed_password"
        ]
        
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name'}),
            'second_name': TextInput(attrs={'placeholder': 'Second Name'}),
            'email': TextInput(attrs={'placeholder': 'Enter Email'}),
            'phone_number': TextInput(attrs={'placeholder': 'Phone Number'}),
            'hashed_password': TextInput(attrs={'placeholder': 'Password'}),
        }
        
        labels = {
            "first_name": '',
            "second_name": '',
            "email": '', 
            "phone_number": '', 
            "hashed_password": ''
        }