from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    hashed_password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    session_id = models.CharField(max_length=100, blank=True, null=True)
    reset_token = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)