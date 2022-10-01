from .models import *
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



# 댓글 입력 폼
class CommentModelForm(ModelForm):
    class Meta:
        # To specify the model to be used to create form  
        model = CommentModel
        # It includes all the fields of model  
        fields = ['comment',]
        # exclude = ('nickname','owner','pub_date','is_public')
        

# 서치 폼
class SearchForm(forms.Form):
    word = forms.CharField(label='Search Word')
    