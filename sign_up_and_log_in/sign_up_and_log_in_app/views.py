from django.shortcuts import render, redirect
from .models import User
from .signUpForm import UserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'sign_up_and_log_in_app/index.html')

def sign_up_page(request):
    form = UserForm()
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})

def log_in_page(request):
    return render(request, 'sign_up_and_log_in_app/log_in.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            hashed_password = form.cleaned_data['hashed_password']
            User.objects.create(first_name=first_name, second_name=second_name, email=email, phone_number=phone_number, hashed_password=hashed_password)
            messages.success(request, "Sign up successful! Please log in")
            return redirect('log_in_page')
    else:
        form = UserForm(request.POST)
        return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})