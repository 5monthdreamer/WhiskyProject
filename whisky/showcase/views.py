from django.shortcuts import render, redirect, get_object_or_404
# image form 저장
from showcase.forms import * 
from showcase.models import *

# Create your views here.
def show(request):
    
    if request.user.is_authenticated:
        
        obj = UploadImageModel.objects.exclude(owner__isnull=True)
        images = obj.filter(is_public=True).order_by('-pub_date')
        

        return render(request, 'showcase/showcase.html', {'images':images})

    else:
        error_message = "※ If you want to use more fantastic functions, Sign in!"
        
        return render(request, 'showcase/showcase.html', {'error_message':error_message})

