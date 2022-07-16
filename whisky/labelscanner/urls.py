from django.urls import path  
from . import views
  
app_name = 'labelscanner'  
urlpatterns = [  
    path('', views.img_scanning, name="main_labelscanner"),
    # path('m', views.mobile_show, name="mobile_main_labelscanner")

]