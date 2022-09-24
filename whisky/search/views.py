# Create your views here.
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



def search_main(request):
    m ="m"
    return render(request, 'search/search_main.html', {"p":m})