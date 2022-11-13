"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
# from django_sitemaps import robots_txt
from .sitemap import * 
from django.contrib.sitemaps.views import sitemap



from . import views



sitemaps = { 'static':StaticViewSitemap, }


urlpatterns = [
    # path('__debug__/',include('debug_toolbar.urls')), # 장고디버그툴바 사용
    path('admin/', admin.site.urls),
    path('',views.home_main,name='home'),
    path('robots.txt',  TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('common/',include('common.urls')),
    path('showcase/',include('showcase.urls')),
    path('labelcanner/',include('labelscanner.urls')),
    path('tastingnote/',include('tastingnote.urls')),
    path('search/',include('search.urls')),
    path('save/<int:imagemodel_id>',views.home_imagesave,name='home_imagesave'), #이미지 follow
    path('like/<int:imagemodel_id>',views.home_imagelike,name='home_imagelike'), #이미지 like
    path('save/<int:notemodel_id>',views.home_notesave,name='home_notesave'), #노트 저장
    path('savecomment/<int:imagemodel_id>',views.home_imagecomment,name='home_imagecomment'), #댓글 저장
    path('ads.txt',  TemplateView.as_view(template_name="ads.txt", content_type='text/plain')), #대망의 adsense


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)