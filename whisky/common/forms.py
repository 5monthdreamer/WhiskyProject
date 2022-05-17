from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):
    # email = forms.EmailField(label="이메일")
    # nickname = forms.CharField(max_length=50, required=True)
    

    class Meta:
        model = get_user_model()
        fields = ("username", "nickname", "password1", "password2", "email")
        
        


