from .models import UploadImageModel, TastingNoteModel
from django.forms import ModelForm
from django import forms


  
class UserImageForm(ModelForm):
    class Meta:
        # To specify the model to be used to create form  
        model = UploadImageModel
        # It includes all the fields of model  
        fields = ['image','whiskyname',]
        # exclude = ('nickname','owner','pub_date','is_public')
        
        
        Widget = {
            'image' : forms.FileInput(attrs={'class':'form-control'})
            
        }


# 위스키 이름만 부여하기 위한 폼
class UserwhiskynameForm(ModelForm):
    class Meta:
        # To specify the model to be used to create form  
        model = UploadImageModel
        # It includes all the fields of model  
        fields = ['whiskyname',]
        # exclude = ('nickname','owner','pub_date','is_public')
        
        



class UserTastingNoteForm(ModelForm):
    

    
    class Meta:
        # To specify the model to be used to create form  
        model = TastingNoteModel
        
        # It includes all the fields of model  
        fields = ['name','drumtong_rating','one_line_review','taste','taste_intensity','flavor','flavor_intensity','alchol_finish',]



        
        
    
# def __init__(self, ids, *args,**kwargs):
#     super(UserTastingNoteForm, self).__init__(*args,**kwargs)
#     self.fields['UploadImageModel'].queryset = UploadImageModel.objects.get(id=ids)

# def __init__(self, imagemodel=None, *args,**kwargs):
#     user = kwargs.pop('user','')
#     super(UserTastingNoteForm, self).__init__(*args,**kwargs)
#     self.fields['UploadImagekey'] = forms.ModelChoiceField(queryset=UploadImageModel.objects.get(pk=imageid))