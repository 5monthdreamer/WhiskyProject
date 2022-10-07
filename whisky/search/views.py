# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, FormView

from django.shortcuts import  render, get_object_or_404, redirect
from django.urls import reverse

# image form 저장
from showcase.forms import *
from showcase.models import *


# pagination 설정
from django.core.paginator import Paginator

# Django ORM
from django.db.models import F, Sum, Count, Case, When, Q

from django.contrib.auth import get_user_model




# 이제 Post대신 검색프로세스 코딩하면 됨
class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'search/search_main.html'

    def form_valid(self,form): # post method로 값이 전달 됬을 경우
        word = '%s' %self.request.POST['word'] # 검색어
        
        User = get_user_model()
        owner_list = User.objects.filter(
            Q(username__icontains=word) | Q(nickname__icontains=word)
            # Q 객체를 사용해서 검색한다.
            # owner 칼럼에 대소문자를 구분하지 않고  단어가 포함되어있는지 (icontains) 검사
        ).distinct() #중복을 제거한다.
        
               
        whiskyname_list = UploadImageModel.objects.filter(
            Q(is_public=True), Q(whiskyname__icontains=word)
            # Q 객체를 사용해서 검색한다.
            # whiskyname 칼럼에 대소문자를 구분하지 않고  단어가 포함되어있는지 (icontains) 검사
        ).distinct() #중복을 제거한다.

        note_list = TastingNoteModel.objects.filter(
            Q(is_public=True),
            Q(name__icontains=word) | Q(one_line_review__icontains=word) | Q(drumtong_rating__icontains=word) | Q(taste__icontains=word) | Q(taste_intensity__icontains=word) | Q(flavor__icontains=word) | Q(flavor_intensity__icontains=word) | Q(etc__icontains=word) | Q(etc_intensity__icontains=word) | Q(long_review__icontains=word)
            # Q 객체를 사용해서 검색한다.
            # whiskyname 칼럼에 대소문자를 구분하지 않고  단어가 포함되어있는지 (icontains) 검사
        ).distinct() #중복을 제거한다.
        
        # note_list = note_list_before.filter(is_public=True)
        
        
        comment_list = CommentModel.objects.filter(
            Q(comment__icontains=word)
            # Q 객체를 사용해서 검색한다.
            # whiskyname 칼럼에 대소문자를 구분하지 않고  단어가 포함되어있는지 (icontains) 검사
        ).distinct() #중복을 제거한다.
        
                
                
        context = {}
        context['search_word']= word # 검색어를 컨텍스트 변수에 담는다.
        context['owner_list'] = owner_list # 검색된 결과를 컨텍스트 변수에 담는다.
        context['whiskyname_list'] = whiskyname_list # 검색된 결과를 컨텍스트 변수에 담는다.
        context['note_list'] = note_list # 검색된 결과를 컨텍스트 변수에 담는다.
        context['comment_list'] = comment_list # 검색된 결과를 컨텍스트 변수에 담는다.
        
        return render(self.request, 'search/search_main.html', context)
    
    
    
        # whiskyname_list = UploadImageModel.objects.filter(
        #     Q(whiskyname__icontains=word)
        #     # Q 객체를 사용해서 검색한다.
        #     # whiskyname 칼럼에 대소문자를 구분하지 않고  단어가 포함되어있는지 (icontains) 검사
        # ).distinct() #중복을 제거한다.
        
        # note_list = TastingNoteModel.objects.filter(
        #     Q(name__icontains=word) | Q(one_line_review__icontains=word) | Q(etc__icontains=word) | Q(long_review__icontains=word)
        #     # Q 객체를 사용해서 검색한다.
        #     # whiskyname 칼럼에 대소문자를 구분하지 않고  단어가 포함되어있는지 (icontains) 검사
        # ).distinct() #중복을 제거한다.
