from django.views.generic.base import TemplateView

from django.shortcuts import  render, get_object_or_404, redirect
from django.urls import reverse

# image form 저장
from showcase.forms import *
from showcase.models import *


# pagination 설정
from django.core.paginator import Paginator






class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['labelscanner','showcase']
        return context





def home_main(request):
    
    obj = UploadImageModel.objects.exclude(owner__isnull=True)
    images_public = obj.filter(is_public=True)

    paginator = Paginator(images_public,9)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    
    
    try:
        follow = ImageFollowModel.objects.filter(follower=request.user)
                                                         
        return render(request, 'home.html', {'images':images, 'follow':follow})
    
    except:
        
        return render(request, 'home.html', {'images':images})
    




def home_imagesave(request, imagemodel_id):
    
    the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=True)
    # ImageFollowModel.UploadImagekey = the_UploadImageModel
    
    try:
        the_ImageFollowModel = get_object_or_404(ImageFollowModel, UploadImagekey_id = imagemodel_id, follower=request.user)
        
        if the_ImageFollowModel.is_follow == True:
            the_ImageFollowModel.is_follow = False
            the_ImageFollowModel.save()
        else:
            the_ImageFollowModel.is_follow = True
            the_ImageFollowModel.save()

    except:
        the_ImageFollowModel = ImageFollowModel()
        the_ImageFollowModel.UploadImagekey = the_uploadimagemodel
        the_ImageFollowModel.follower = request.user
        the_ImageFollowModel.is_follow = True
        the_ImageFollowModel.save()
    
    return redirect(reverse('home'))


def home_imagelike(request, imagemodel_id):
    
    the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=True)
    # ImageFollowModel.UploadImagekey = the_UploadImageModel
    
    try:
        the_ImagelikeModel = get_object_or_404(ImageFollowModel, UploadImagekey_id = imagemodel_id, follower=request.user)
        
        if the_ImagelikeModel.is_like == True:
            the_ImagelikeModel.is_like = False
            the_ImagelikeModel.save()
        else:
            the_ImagelikeModel.is_like = True
            the_ImagelikeModel.save()

    except:
        the_ImagelikeModel = ImageFollowModel()
        the_ImagelikeModel.UploadImagekey = the_uploadimagemodel
        the_ImagelikeModel.follower = request.user
        the_ImagelikeModel.is_like = True
        the_ImagelikeModel.save()
    
    return redirect(reverse('home'))
 


def home_notesave(request, notemodel_id):

    the_tastingnotemodel = get_object_or_404(NoteFollowModel, pk=notemodel_id, is_public=True)
    # ImageFollowModel.UploadImagekey = the_UploadImageModel
    
    try:
        the_notefollowmodel = get_object_or_404(NoteFollowModel, UploadNotekey_id = notemodel_id, follower=request.user, is_follow = True)     
        the_notefollowmodel.delete()

    except:
        the_notefollowmodel = ImageFollowModel()
        the_notefollowmodel.UploadImagekey = the_tastingnotemodel
        the_notefollowmodel.follower = request.user
        the_notefollowmodel.is_follow = True
        the_notefollowmodel.save()
    
    return redirect(reverse('home'))





        
    






