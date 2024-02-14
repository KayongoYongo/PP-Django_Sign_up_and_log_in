from django.shortcuts import render

# Create your views here.
def home(request):
    return render(reqest, 'sign_up_and_log_in_app/index.html')
