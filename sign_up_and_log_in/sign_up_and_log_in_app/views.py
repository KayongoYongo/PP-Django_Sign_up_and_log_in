from django.shortcuts import render, redirect
from .models import User
from .signUpForm import UserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    return render(request, 'sign_up_and_log_in_app/index.html')

def sign_up_page(request):
    form = UserForm()
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})

def log_in_page(request):
    return render(request, 'sign_up_and_log_in_app/log_in.html')

def sign_up(request):
    print(UserForm)
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.data)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password_1']
            hashed_password = make_password(password)
            User.objects.create(user_name=user_name, email=email, password=hashed_password)
            messages.success(request, "Sign up successful! Please log in")
            print(user_name,email,password)
            return redirect('log_in_page')
    else:
        form = UserForm()
        
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})