from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class Employee(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)
    
    
# class CustomUser(AbstractUser):
#     pass