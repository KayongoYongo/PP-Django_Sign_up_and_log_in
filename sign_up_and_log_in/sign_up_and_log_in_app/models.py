from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True, blank=True, error_messages={'unique':"This email is already registered."})
    password = models.CharField(max_length=128, blank=True)
    user_name = models.CharField(max_length=50, blank=True)
    session_id = models.CharField(max_length=100, blank=True, null=True)
    reset_token = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)