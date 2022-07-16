from django.shortcuts import render, redirect
# image form 저장
from showcase.forms import UserImageForm  
from showcase.models import UploadImageModel 

# Create your views here.
def show(request):
    form = UserImageForm()
    images = UploadImageModel.objects.all()
    return render(request, 'showcase/showcase.html', {'form':form, 'images':images})

def mobile_show(request):
    form = UserImageForm()
    images = UploadImageModel.objects.all()
    return render(request, 'showcase/mobileshowcase.html', {'form':form, 'images':images})