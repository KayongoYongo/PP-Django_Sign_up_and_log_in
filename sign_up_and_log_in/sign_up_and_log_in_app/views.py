from django.shortcuts import render, redirect
from .signUpForm import signUpForm
from .logInForm import logInForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

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
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Sign up successful! Please log in")
            print(username,email,password)
            return redirect('log_in_page')
        print(len(form.errors))
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

            # Check if a user with the provided email exists
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user is not None:
                user = authenticate(request, username=user.username, password=password)
                print("The user is", user)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Log in successful!")
                    return redirect('home')
                else:
                    # Authentication failed
                    print('wrong credentials')
                    messages.error(request, "Invalid email or password")
                    return redirect('log_in_page')
            else:
                # User with the provided email does not exist
                messages.error(request, "No user with this email exists")

        # Form data invalid, display form with errors
        return render(request, 'sign_up_and_log_in_app/log_in.html', {'form': form})
    else:
        # GET request, display empty form
        form = logInForm()
    return render(request, 'sign_up_and_log_in_app/log_in.html', {'form' : form})

def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('home')