from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),  #로그인뷰 따로 만들필요 없음 대박
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('qna/', views.qna_main, name='qna_main'),
    path('pofileimage_edit/', views.pofileimage_edit, name='pofileimage_edit'),
]
