from django.urls import path  
from . import views


app_name = 'tastingnote'  
urlpatterns = [  
    path('<int:UploadImagekey_id>/', views.tastingnote_write, name="main_tastingnote"),
    
    # path('m', views.mobile_tastingnote_write, name="mobile_main_tastingnote"),
]