from django.shortcuts import render, redirect, get_object_or_404
# image form 저장
from showcase.forms import * 
from showcase.models import *

# Create your views here.
def show(request):
    obj = UploadImageModel.objects.exclude(owner__isnull=True)
    images = obj.filter(is_public=True)
    

    return render(request, 'showcase/showcase.html', {'images':images})


