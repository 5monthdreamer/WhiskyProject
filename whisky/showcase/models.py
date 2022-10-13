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
    image = models.ImageField(upload_to='', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)  # 사용자가 입력하지 않고 업로드 하는 순간 자동으로 세팅이 됨.
    is_public = models.BooleanField(default=False)      # 비공개 사진인지, 공개 사진인지에 대한 필드
    # nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    whiskyname = models.CharField(max_length=100, blank=True, null=True)
    
    
    
    # <수정 전>
    # owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, default=0) # 하나의 사진은 한명의 사용자에게 속해야 하므로. 1:N의 관계
    
    # def __str__(self):
    #     return self.image
    

  
class TastingNoteModel(models.Model):
    
    UploadImagekey = models.ForeignKey(UploadImageModel, on_delete=models.CASCADE)
    # notekey = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, db_column="note_id")
    name = models.CharField(max_length=100) #required 넣기!!
    drumtong_rating = models.IntegerField()
    one_line_review = models.CharField(max_length=100)
    taste = models.CharField(max_length=20)
    taste_intensity = models.IntegerField()
    flavor = models.CharField(max_length=20)
    flavor_intensity = models.IntegerField()
    alchol_finish = models.IntegerField()
    long_review = models.CharField(max_length=1000, blank=True, null=True)
    
    etc = models.CharField(max_length=50, blank=True, null=True)
    etc_intensity = models.CharField(max_length=50, blank=True, null=True)

    pub_date = models.DateTimeField(auto_now_add=True)  # 사용자가 입력하지 않고 업로드 하는 순간 자동으로 세팅이 됨.
    is_public = models.BooleanField(default=False)      # 비공개 사진인지, 공개 사진인지에 대한 필드

    

class ImageFollowModel(models.Model): 
    follower = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, blank=False, null=False) # 하나의 사진은 여려명의 팔로워에게 속할 수 있음. 1:N의 관계
    UploadImagekey = models.ForeignKey(UploadImageModel, on_delete=models.CASCADE) # 팔로우 이미지
    is_follow = models.BooleanField(default=False) # 팔로우 여부
    is_like = models.BooleanField(default=False) # 좋아요 여부
    
    
    
    
# class ImageCommentModel(models.Model): 
#     UploadImagekey = models.ForeignKey(ImageFollowModel, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=20, blank=True, null=True)


class UserFollowModel(models.Model): 
    User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, null=False, related_name='following') # 팔로우 이미지
    follower = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,  blank=False, null=False, related_name='followers') # 하나의 사진은 여려명의 팔로워에게 속할 수 있음. 1:N의 관계



# 댓글모델을 따로 만들기!!
class CommentModel(models.Model):
    UploadImagekey = models.ForeignKey(UploadImageModel, on_delete=models.CASCADE) # 팔로우 이미지
    comment_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, blank=False, null=False) # 하나의 사진은 여려명의
    comment = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
class CommentlikeModel(models.Model): 
    commentmodelkey = models.ForeignKey(CommentModel, on_delete=models.CASCADE) # 팔로우 이미지
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, blank=False, null=False) # 하나의 사진은 여려명의 팔로워에게 속할 수 있음. 1:N의 관계
    is_like = models.BooleanField(default=False) # 좋아요 여부

# 대댓글모델
class CommentCommentModel(models.Model): 
    commentmodelkey = models.ForeignKey(CommentModel, on_delete=models.CASCADE) # 팔로우 이미지
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, blank=False, null=False) # 하나의 사진은 여려명의 팔로워에게 속할 수 있음. 1:N의 관계
    usercomment = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

class CommentCommentlikeModel(models.Model): 
    commentcommentmodelkey = models.ForeignKey(CommentModel, on_delete=models.CASCADE) # 팔로우 이미지
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, blank=False, null=False) # 하나의 사진은 여려명의 팔로워에게 속할 수 있음. 1:N의 관계
    is_like = models.BooleanField(default=False) # 좋아요 여부






# Q&A Question
class qnaquestionmodel(models.Model):
    questioner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_constraint=False, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    question_title = models.CharField(max_length=50)
    question = models.CharField(max_length=1000)

# Q&A Answer
class qnaanswermodel(models.Model):
    qnaquestionkey = models.ForeignKey(qnaquestionmodel, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    answer = models.CharField(max_length=1000, blank=True, null=True)