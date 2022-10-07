from django.contrib import admin

# Register your models here.
from showcase.models import *

admin.site.register(UploadImageModel)
admin.site.register(TastingNoteModel)
admin.site.register(ImageFollowModel)
admin.site.register(UserFollowModel)
admin.site.register(CommentModel)
admin.site.register(CommentlikeModel)
admin.site.register(CommentCommentModel)
admin.site.register(CommentCommentlikeModel)
admin.site.register(qnaquestionmodel)
admin.site.register(qnaanswermodel)
