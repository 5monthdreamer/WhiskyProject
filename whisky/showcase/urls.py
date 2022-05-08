from django.urls import path  
from . import views
  
app_name = 'showcase'  
urlpatterns = [  
    path('', views.show, name="main_showcase"),
    path('m', views.mobile_show, name="mobile_main_showcase")

]