from django.db import models
from common.forms import UserForm


# Create your models here.

class UploadImageModel(models.Model):  
    # file = models.FileField(upload_to='documents/', null=True)
    image = models.ImageField(upload_to='', null=True)
    

  

    
