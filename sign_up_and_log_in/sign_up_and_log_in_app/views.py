from django.shortcuts import render, redirect
from .models import User
from .signUpForm import signUpForm
from .logInForm import logInForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    return render(request, 'sign_up_and_log_in_app/index.html')

def sign_up_page(request):
    form = signUpForm()
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})

def log_in_page(request):
    form = logInForm()
    return render(request, 'sign_up_and_log_in_app/log_in.html', {'form': form})

def sign_up(request):
    print(signUpForm)
    if request.method == 'POST':
        form = signUpForm(request.POST)
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
        form = signUpForm()
        
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})

def log_in(request):
    print(logInForm)
    if request.method == 'POST':
        form = logInForm(request.POST)
        print(form.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Log in successful!")
                return redirect('home')
            else:
                # Authentication failed
                error_message = "Invalid username or password."
                return render(request, 'sign_up_and_log_in_app/log_in.html', {'error_message': error_message})
    else:
        form = logInForm()
    
    return render(request, 'sign_up_and_log_in_app/log_in.html', {'form' : form})