from ssl import HAS_TLSv1_1
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

# 이미지 경로 지정
from django.core.files.storage import FileSystemStorage

# image form 저장
from showcase.forms import *  
from showcase.models import *

from django.db.models import Count

# pagination 설정
from django.core.paginator import Paginator

# 유저모델 사용
from django.contrib.auth import get_user_model



# Create your views here.
def tastingnote(request):

    obj = UploadImageModel.objects.filter(owner=request.user)
    
    paginator = Paginator(obj,9)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    
    
    following = UserFollowModel.objects.filter(User=request.user).count()
    followers = UserFollowModel.objects.filter(follower=request.user).count()
    
    return render(request, 'tastingnote/tastingnote_main.html', {'images':images, 'following':following, 'followers':followers})
        
    # 유저가 비로그인일때 해결방법
    # if request.user:
    # else:
    #     return render(request, 'tastingnote/tastingnote_main.html')
    
    

   
    
# Create your views here.
def tastingnote_write(request, UploadImagekey_id):
    
    the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)
    
    
    fss = FileSystemStorage()
    file_url = fss.url(the_uploadimagemodel.image)
    

    # form = UserTastingNoteForm()
    # form.UploadImageModel.queryset = UploadImageModel.objects.filter(UploadImagekey_id=UploadImagekey_id)


    # 사용자만 볼 수 있는 조건식
    if the_uploadimagemodel.owner == request.user:
        
        if request.method == 'POST':
            
            form1 = UserwhiskynameForm(request.POST)
            form2 = UserTastingNoteForm(request.POST)
            
            # form.fields['UploadImagekey'].queryset = UploadImageModel.objects.filter(pk=UploadImagekey_id)
            
            
            
            # form.save()
            if form1.is_valid() and form2.is_valid():  

                global note
                note = form2.save(commit=False)
                note.UploadImagekey = the_uploadimagemodel
                form2.save()
                note.save()
                

                
                # <위스키이름 수정방법은??ㅜㅜ form을 하나밖에 못씀. 새로운 폼을 만들자>
                # <노트 추가 저장>
                the_uploadimagemodel.whiskyname = form1.cleaned_data['whiskyname']
                the_uploadimagemodel.tastingnotemodel_set.add(note)
                the_uploadimagemodel.save()

                
                
                # <테이스팅노트 부여>
                name = form2.cleaned_data['name']
                drumtong_rating = form2.cleaned_data['drumtong_rating']
                one_line_review = form2.cleaned_data['one_line_review']
                taste = form2.cleaned_data['taste']
                taste_intensity = form2.cleaned_data['taste_intensity']
                flavor = form2.cleaned_data['flavor']
                flavor_intensity = form2.cleaned_data['flavor_intensity']
                alchol_finish = form2.cleaned_data['alchol_finish']
                

                

                return render(request, 'tastingnote/tastingnote.html', {'name':name, 'drumtong_rating': drumtong_rating, 'one_line_review':one_line_review, 'taste':taste, 'taste_intensity':taste_intensity, 'flavor':flavor, 'flavor_intensity':flavor_intensity, 'alchol_finish':alchol_finish, 'the_uploadimagemodel':the_uploadimagemodel, 'file_url':file_url})
                

                
        else:
                
            # return render(request, 'tastingnote/tastingnote.html')
        
            form1 = UserwhiskynameForm()
            form2 = UserTastingNoteForm()
            
            return render(request, 'tastingnote/tastingnote.html', {'form1':form1, 'form2':form2, 'tastingnote':tastingnote, 'the_uploadimagemodel':the_uploadimagemodel, 'file_url':file_url})
    
    else:
        return render(request, 'labelscanner/labelscanner.html')
        
    
    
    
def tastingnote_delete(request, TastingNoteModel_id):
    
    # images = UploadImageModel.objects.filter(owner=request.user)

    
    the_tastingNoteModel = get_object_or_404(TastingNoteModel, pk=TastingNoteModel_id)

    if the_tastingNoteModel.UploadImagekey.owner == request.user:
        the_tastingNoteModel.delete()

    return redirect(reverse('tastingnote:tastingnote'))
        

        

# Create your views here.
def tastingnote_edit(request, TastingNoteModel_id):
    
    
    the_tastingnotemodel = get_object_or_404(TastingNoteModel, pk=TastingNoteModel_id)
    
    the_uploadimagemodel = get_object_or_404(UploadImageModel, pk=the_tastingnotemodel.UploadImagekey.id)
    
    
    fss = FileSystemStorage()
    file_url = fss.url(the_uploadimagemodel.image)
    

    # form = UserTastingNoteForm()
    # form.UploadImageModel.queryset = UploadImageModel.objects.filter(UploadImagekey_id=UploadImagekey_id)


    # 사용자만 볼 수 있는 조건식
    if the_uploadimagemodel.owner == request.user:
        
        if request.method == 'POST':
            
            form = UserTastingNoteForm(request.POST)
            
            # form.fields['UploadImagekey'].queryset = UploadImageModel.objects.filter(pk=UploadImagekey_id)
            
            # form.save()
            if form.is_valid():  

                # global note
                # note = form.save(commit=False)
                # note.UploadImagekey = the_uploadimagemodel
                # form.save()
                # note.save()
                
                
                the_tastingnotemodel.name = form.cleaned_data['name']
                the_tastingnotemodel.drumtong_rating = form.cleaned_data['drumtong_rating']
                the_tastingnotemodel.one_line_review = form.cleaned_data['one_line_review']
                the_tastingnotemodel.taste = form.cleaned_data['taste']
                the_tastingnotemodel.taste_intensity = form.cleaned_data['taste_intensity']
                the_tastingnotemodel.flavor = form.cleaned_data['flavor']
                the_tastingnotemodel.flavor_intensity = form.cleaned_data['flavor_intensity']
                the_tastingnotemodel.alchol_finish = form.cleaned_data['alchol_finish']
                the_tastingnotemodel.save()
                
                # form.save()
                
                # review.save()
                # sweetness.save()
                # acidity.save()
                # alchol.save()
                
                
                
                # record = UploadImageModel.objects.all()
                # record.delete()
                # form.save()  #form.save(commit=False)
                

                return render(request, 'tastingnote/tastingnote.html', {'the_uploadimagemodel':the_uploadimagemodel, 'the_tastingnotemodel':the_tastingnotemodel, 'file_url':file_url})
                

                
        else:
                
            # return render(request, 'tastingnote/tastingnote.html')
        
            form = UserTastingNoteForm()
            
            return render(request, 'tastingnote/tastingnote.html', {'form':form, 'the_uploadimagemodel':the_uploadimagemodel, 'the_tastingnotemodel':the_tastingnotemodel, 'file_url':file_url})
    


def tastingnote_public(request, TastingNoteModel_id):
    

    # images = UploadImageModel.objects.filter(owner=request.user)

    the_tastingnotemodel = get_object_or_404(TastingNoteModel, pk=TastingNoteModel_id)

    if the_tastingnotemodel.UploadImagekey.owner == request.user:

        if the_tastingnotemodel.is_public == False:
            the_tastingnotemodel.is_public = True
            the_tastingnotemodel.save()
        else:
            the_tastingnotemodel.is_public = False
            the_tastingnotemodel.save()
            
        
    return redirect(reverse('tastingnote:tastingnote'))





        
    
def whisky_delete(request, UploadImagekey_id):
    

    # images = UploadImageModel.objects.filter(owner=request.user)

    the_UploadImageModel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)

    if the_UploadImageModel.owner == request.user:
        the_UploadImageModel.delete()
        
    return redirect(reverse('tastingnote:tastingnote'))



def whisky_public(request, UploadImagekey_id):
    

    # images = UploadImageModel.objects.filter(owner=request.user)

    the_UploadImageModel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)

    if the_UploadImageModel.owner == request.user:

        if the_UploadImageModel.is_public == False:
            the_UploadImageModel.is_public = True
            the_UploadImageModel.save()
        else:
            the_UploadImageModel.is_public = False
            the_UploadImageModel.save()
            
        
    return redirect(reverse('tastingnote:tastingnote'))



def whisky_edit(request, UploadImagekey_id):
    
    
    the_UploadImageModel = get_object_or_404(UploadImageModel, pk=UploadImagekey_id, owner=request.user)
    
    if request.method == 'POST' and request.FILES:
        form = UserImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            if request.user.is_authenticated:
                form.owner = request.user
            else:
                pass
            
            form.save()
            
            the_UploadImageModel.image = form.cleaned_data['image']
            the_UploadImageModel.whiskyname = form.cleaned_data['whiskyname']
            the_UploadImageModel.save()
            
            return redirect(reverse('tastingnote:tastingnote'))
        
    else:
        form = UserImageForm()
        
        return render(request, 'tastingnote/tastingnote_whiskyedit.html', {'the_UploadImageModel': the_UploadImageModel, 'form':form})
            

    
# Create your views here.
def tastingnote_user(request,user_id):

    obj = UploadImageModel.objects.filter(owner = user_id, is_public=True)
    
    paginator = Paginator(obj,9)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    
    User = get_user_model()
    tastingnoteuser = User.objects.get(pk = user_id)
    
    followers = UserFollowModel.objects.filter(User=tastingnoteuser).count()
    following = UserFollowModel.objects.filter(follower=tastingnoteuser).count()
    
    return render(request, 'tastingnote/tastingnote_user.html', {'images':images, 'following':following, 'followers':followers, 'tastingnoteuser':tastingnoteuser}) 



def tastingnote_userfollow(request, userfollow_id):
    
   
    try:
        the_userfollowmodel = get_object_or_404(UserFollowModel, User_id = userfollow_id, follower=request.user)     
        the_userfollowmodel.delete()

    except:
        User = get_user_model()
        followmodel = UserFollowModel()
        
        if User.objects.get(pk = userfollow_id) == request.user:
            pass
        else:
            followmodel.User = User.objects.get(pk = userfollow_id)
            followmodel.follower = request.user
            followmodel.save()
    
    return redirect('tastingnote:user_tastingnote', userfollow_id)