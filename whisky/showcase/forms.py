 
from tkinter import Widget

from attr import attr, attrs
from .models import UploadImageModel  
from django.forms import ModelForm
from django import forms


  
class UserImageForm(ModelForm):
    class Meta:
        # To specify the model to be used to create form  
        model = UploadImageModel
        # It includes all the fields of model  
        fields = ['image',]
        # exclude = ('nickname','owner','pub_date','is_public')
        
        
        Widget = {
            'image' : forms.FileInput(attrs={'class':'form-control'})
            
        }
