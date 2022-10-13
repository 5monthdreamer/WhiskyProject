from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# import all model, form
from showcase.forms import *
from showcase.models import *
from common.forms import *

# pagination 설정
from django.core.paginator import Paginator

# Django ORM
from django.db.models import F, Sum, Count, Case, When

# 이미지저장
from django.core.files.storage import FileSystemStorage

# 유저모델
from django.contrib.auth import get_user_model


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})



def qna_main(request):
    

    # 댓글 폼과 모델
    form = qnaquestionform()
    questionmodel = qnaquestionmodel.objects.all()
    model = questionmodel.order_by('-pub_date')
    
    paginator = Paginator(model,10)
    page = request.GET.get('page')
    question = paginator.get_page(page)
    
    if request.method == 'POST':
        form = qnaquestionform(request.POST)
        
        if form.is_valid():
            note = form.save(commit=False)
            note.questioner = request.user
            note.save()
            
    
    return render(request, 'common/QnA.html', {'question':question, 'form':form})



def pofileimage_edit(request):
    if request.user.is_authenticated:        
        if request.method == "POST" and request.FILES:
            form = UserProfileForm(request.POST, request.FILES, instance = request.user)
            if form.is_valid():
                form.save()
                # user = form.save(commit=False)
                # user.save()
                # model.profileimage = form.cleaned_data['profileimage']
                # model.save()
                
                # saved_image = form.cleaned_data['profileimage']
                # fss = FileSystemStorage()
                # file_url = fss.url(saved_image)
                
    return redirect('tastingnote:tastingnote')