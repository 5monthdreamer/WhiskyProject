 
from .models import UploadImageModel  
from django.forms import ModelForm



  
class UserImageForm(ModelForm):
    class Meta:
        # To specify the model to be used to create form  
        model = UploadImageModel
        # It includes all the fields of model  
        fields = ('image',) 