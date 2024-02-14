from django.shortcuts import render
from .models import User
from .signUpForm import UserForm

# Create your views here.
def home(request):
    return render(request, 'sign_up_and_log_in_app/index.html')

def sign_up_page(request):
    form = UserForm()
    return render(request, 'sign_up_and_log_in_app/sign_up.html', {'form' : form})

def sign_up(request):
    pass