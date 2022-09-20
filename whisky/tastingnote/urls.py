from django.urls import path  
from . import views


app_name = 'tastingnote'  
urlpatterns = [  
    path('', views.tastingnote, name="tastingnote"),
    path('<int:UploadImagekey_id>/', views.tastingnote_write, name="main_tastingnote"),
    path('<int:TastingNoteModel_id>/delete', views.tastingnote_delete, name="delete_tastingnote"),
    path('<int:TastingNoteModel_id>/edit', views.tastingnote_edit, name="edit_tastingnote"),
    path('<int:TastingNoteModel_id>/public', views.tastingnote_public, name="public_tastingnote"),

    path('<int:UploadImagekey_id>/deletewhisky', views.whisky_delete, name="delete_whisky"),
    path('<int:UploadImagekey_id>/editwhisky', views.whisky_edit, name="edit_whisky"),
    path('<int:UploadImagekey_id>/publicwhisky', views.whisky_public, name="public_whisky"),
    
    path('user/<int:user_id>', views.tastingnote_user, name="user_tastingnote"),
    path('userfollow/<int:userfollow_id>', views.tastingnote_userfollow, name="userfollow_tastingnote"),
    
    
    # path('m', views.mobile_tastingnote_write, name="mobile_main_tastingnote"),
]