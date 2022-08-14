from tkinter import CASCADE
from django.db import models
from common.forms import UserForm
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

class UploadImageModel(models.Model):  
    # file = models.FileField(upload_to='documents/', null=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, blank=True, null=True) # 하나의 사진은 한명의 사용자에게 속해야 하므로. 1:N의 관계
    # imagekey = models.ForeignKey(self, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='', null=True)
    pub_date = models.DateTimeField(auto_now_add=True)  # 사용자가 입력하지 않고 업로드 하는 순간 자동으로 세팅이 됨.
    is_public = models.BooleanField(default=False)      # 비공개 사진인지, 공개 사진인지에 대한 필드
    # nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    
    
    # <수정 전>
    # owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, default=0) # 하나의 사진은 한명의 사용자에게 속해야 하므로. 1:N의 관계
    
    # def __str__(self):
    #     return self.image

  
class TastingNoteModel(models.Model):
    
    UploadImagekey = models.ForeignKey(UploadImageModel, related_name="UploadImageModel", on_delete=models.CASCADE)
    # notekey = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, db_column="note_id")
    name = models.CharField(max_length=20) #required 넣기!!
    drumtong_rating = models.IntegerField()
    one_line_review = models.CharField(max_length=50)
    taste = models.CharField(max_length=20)
    taste_intensity = models.IntegerField()
    flavor = models.CharField(max_length=20)
    flavor_intensity = models.IntegerField()
    alchol_finish = models.IntegerField()
    long_review = models.CharField(max_length=300, blank=True, null=True)
    
    etc = models.CharField(max_length=50, blank=True, null=True)
    etc_intensity = models.CharField(max_length=50, blank=True, null=True)

    pub_date = models.DateTimeField(auto_now_add=True)  # 사용자가 입력하지 않고 업로드 하는 순간 자동으로 세팅이 됨.
    is_public = models.BooleanField(default=False)      # 비공개 사진인지, 공개 사진인지에 대한 필드

    
