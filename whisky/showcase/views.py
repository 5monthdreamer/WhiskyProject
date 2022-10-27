from django.shortcuts import render, redirect, get_object_or_404
# image form 저장
from showcase.forms import * 
from showcase.models import *
from common.forms import *  


from django.db.models import Count

# pagination 설정
from django.core.paginator import Paginator

# 유저모델 사용
from django.contrib.auth import get_user_model

# Django ORM
from django.db.models import Q, F, Sum, Count, Case, When



# Create your views here.
def show(request):
    
    # 유저 프로필이미지 폼
    form = UserProfileForm()
    
    # 댓글 폼
    form2 = CommentModelForm()
    
    
    if request.user.is_authenticated:
        
        obj1 = UploadImageModel.objects.exclude(owner__isnull=True)
        obj2 = obj1.filter(is_public=True)
        obj = obj2.filter(
            Q(
                imagefollowmodel__is_follow=True,
                imagefollowmodel__follower=request.user
                )
            ).order_by('-pub_date')
        
        paginator = Paginator(obj,9)
        page = request.GET.get('page')
        images = paginator.get_page(page)
        
        # 팔로워,팔로잉숫자 계산
        followers = UserFollowModel.objects.filter(User=request.user).count()
        following = UserFollowModel.objects.filter(follower=request.user).count()
        
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
            
                                                
            return render(request, 'showcase/showcase.html', {'form':form, 'form2':form2, 'images':images, 'following':following, 'followers':followers, 'follow':follow, 'follow_qs':follow_qs, 'followcounting':followcounting, 'likecounting':likecounting})


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
            
            return render(request, 'showcase/showcase.html', {'form':form, 'form2':form2, 'images':images, 'follow_qs':follow_qs, 'followers':followers, 'followcounting':followcounting, 'likecounting':likecounting})


    else:
        error_message = "※ If you want to use more fantastic functions, Sign in!"
        
        return render(request, 'showcase/showcase.html', {'form':form, 'form2':form2, 'error_message':error_message})

