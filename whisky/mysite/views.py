from distutils.log import error
from django.views.generic.base import TemplateView

from django.shortcuts import  render, get_object_or_404, redirect
from django.urls import reverse

# image form 저장
from showcase.forms import *
from showcase.models import *


# pagination 설정
from django.core.paginator import Paginator

# Django ORM
from django.db.models import F, Sum, Count, Case, When




class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['labelscanner','showcase']
        return context





def home_main(request):
    
    obj = UploadImageModel.objects.exclude(owner__isnull=True)
    images_public = obj.filter(is_public=True).order_by('-pub_date')

    paginator = Paginator(images_public,9)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    
    # 댓글 폼과 모델
    form = CommentModelForm()
    commentmodel = CommentModel.objects.all()
    
    try:
        follow = ImageFollowModel.objects.filter(follower=request.user)
        
        # Django DRM 미쳤다... 이래서 django가 중요. DB를 잘 조작하는게 핵심 능력. html은 표현만 할뿐
        
        follow_qs = ImageFollowModel.objects.annotate(
            image=F('UploadImagekey__image')
        ).values(
            'image', 'is_follow', 'is_like'
        )
        
        
        followcounting = follow_qs.filter(
            is_follow = True
        ).values(
            'image'
        ).annotate(
            follow_count = Count('is_follow')
        )
        
        likecounting = follow_qs.filter(
            is_like = True
        ).values(
            'image'
        ).annotate(
            like_count = Count('is_like')
        )
        
                                             
        return render(request, 'home.html', {'images':images, 'follow':follow, 'follow_qs':follow_qs, 'followcounting':followcounting, 'likecounting':likecounting, 'form':form, 'commentmodel':commentmodel})
    
    except:
        
        follow_qs = ImageFollowModel.objects.annotate(
            image=F('UploadImagekey__image')
        ).values(
            'image', 'is_follow', 'is_like'
        )
        
        
        followcounting = follow_qs.filter(
            is_follow = True
        ).values(
            'image'
        ).annotate(
            follow_count = Count('is_follow')
        )
        
        likecounting = follow_qs.filter(
            is_like = True
        ).values(
            'image'
        ).annotate(
            like_count = Count('is_like')
        )
        
        
        return render(request, 'home.html', {'images':images, 'follow_qs':follow_qs, 'followcounting':followcounting, 'likecounting':likecounting, 'form':form, 'commentmodel':commentmodel})
    




def home_imagesave(request, imagemodel_id):
    
    try:
        # (홈화면) 공개된 경우
        the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=True)
        # ImageFollowModel.UploadImagekey = the_UploadImageModel
    
    except:
        try:
            # (테이스팅노트화면) 비공개지만 자기 위스키인 경우
            the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=False, owner=request.user)
        
        except:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
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
    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def home_imagelike(request, imagemodel_id):
    
    try:
        # (홈화면) 공개된 경우
        the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=True)
        # ImageFollowModel.UploadImagekey = the_UploadImageModel
    
    except:
        try:
            # (테이스팅노트화면) 비공개지만 자기 위스키인 경우
            the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=False, owner=request.user)
        
        except:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
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
    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
 


def home_notesave(request, notemodel_id):

    try:
        # 공개된 경우
        the_tastingnotemodel = get_object_or_404(NoteFollowModel, pk=notemodel_id, is_public=True)
        # ImageFollowModel.UploadImagekey = the_UploadImageModel
    
    except:
        try:
            # 비공개지만 자기 위스키인 경우
            the_tastingnotemodel = get_object_or_404(NoteFollowModel, pk=notemodel_id, is_public=False)
            test = get_object_or_404(the_tastingnotemodel, owner=request.user)
            
        except:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            
    try:
        the_notefollowmodel = get_object_or_404(NoteFollowModel, UploadNotekey_id = notemodel_id, follower=request.user, is_follow = True)     
        the_notefollowmodel.delete()

    except:
        the_notefollowmodel = ImageFollowModel()
        the_notefollowmodel.UploadImagekey = the_tastingnotemodel
        the_notefollowmodel.follower = request.user
        the_notefollowmodel.is_follow = True
        the_notefollowmodel.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def home_imagecomment(request, imagemodel_id):
    
    try:
        # (홈화면) 공개된 경우
        the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=True)
        # ImageFollowModel.UploadImagekey = the_UploadImageModel
    
    except:
        try:
            # (테이스팅노트화면) 비공개지만 자기 위스키인 경우
            the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=imagemodel_id, is_public=False, owner=request.user)
        
        except:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        
    if request.method == 'POST':
        form1 = CommentModelForm(request.POST)
    
        if form1.is_valid():
            post = form1.save(commit=False) # 여기서 오류나는 중 해결해야함
            post.UploadImagekey = the_uploadimagemodel
            post.comment_user = request.user
            post.save()

            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        
    