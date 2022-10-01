from django.urls import path
from . import views
from .views import *

app_name = 'search'  
urlpatterns = [  
    path('', SearchFormView.as_view() , name="search_main"),
    
]