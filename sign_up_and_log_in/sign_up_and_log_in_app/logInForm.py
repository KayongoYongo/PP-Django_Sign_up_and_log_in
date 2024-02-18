from django import forms


class logInForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email is None or email.strip() == '':
            raise forms.ValidationError("The email cannot remain empty")

        if password is None or password.strip() == '':
            raise forms.ValidationError("The password cannot remain empty")
        
        if len(password) < 6:
            raise forms.ValidationError("The password cannot be less than 6 characters")

        return cleaned_data