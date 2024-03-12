from django.shortcuts import render, redirect
from .signUpForm import signUpForm
from .logInForm import logInForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from .models import UserProfile
from .userProfileForm import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'sign_up_and_log_in_app/index.html')

def sign_up_page(request):
    form = signUpForm()
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})

def log_in_page(request):
    form = logInForm()
    return render(request, 'sign_up_and_log_in_app/log_in.html', {'form': form})

def user_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    form = UserProfileForm()
    return render(request, 'sign_up_and_log_in_app/user_dashboard.html', {'form': form, 'username': request.user.username, 'user_profile': user_profile})

def sign_up(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        print(form.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # This is an inbuilt Django method that creates a user in the database
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Sign up successful! Please log in")
            print(username,email,password)
            return redirect('log_in_page')
    else:
        # if it is a get request, it displays an empty form
        form = signUpForm()
        
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})

def log_in(request):
    print(logInForm)
    if request.method == 'POST':
        form = logInForm(request.POST)

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

                    # Check if the "Remember me" checkbox is checked
                    remember_me = form.cleaned_data.get('remember_me')

                    if remember_me:
                        # Set a cookie to remember the user's login
                        request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                    else:
                        # Clear any existing session expiration time
                        request.session.set_expiry(0)

                    messages.success(request, "Log in successful!")
                    return redirect('home')
                else:
                    # Authentication failed
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

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Assign the currently logged-in user to the user field
            user_profile.save()
            messages.success(request, 'Image uploaded successfully.')
            return redirect('user_dashboard')
        else:
            form = UserProfileForm()
            print(request.user.username)
    return render(request, 'user_dashboard.html', {'form': form, 'username': request.user.username})

@login_required
def send_email(request):
    subject = 'Email sent successfully'
    message = 'This is the first email.'
    recipient_list = ['sknsammie10@gmail.com']

    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        
    return redirect('home')