from tkinter import CASCADE
from django.db import models
from common.forms import UserForm
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class UploadImageModel(models.Model):  
    # file = models.FileField(upload_to='documents/', null=True)
    image = models.ImageField(upload_to='', null=True)
    nickname = models.CharField(max_length=50, null=True)
    # nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

  

    
