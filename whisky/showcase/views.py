from django.shortcuts import render, redirect
# image form 저장
from showcase.forms import UserImageForm
from showcase.models import UploadImageModel 
from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import get_object_or_404


# Create your views here.
def show(request):
    # user = get_object_or_404(get_user_model())
    form = UserImageForm()
    images = UploadImageModel.objects.all()
    # nickname = get_user_model().nickname
    
    return render(request, 'showcase/showcase.html', {'form':form, 'images':images})

def mobile_show(request):
    form = UserImageForm()
    images = UploadImageModel.objects.all()
    return render(request, 'showcase/mobileshowcase.html', {'form':form, 'images':images})