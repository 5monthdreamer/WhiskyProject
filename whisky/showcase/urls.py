from django.urls import path  
from . import views
  
app_name = 'showcase'  
urlpatterns = [  
    path('', views.show, name="main_showcase"),
]