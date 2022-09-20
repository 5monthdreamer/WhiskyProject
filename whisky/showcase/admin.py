from django.contrib import admin

# Register your models here.
from showcase.models import *

admin.site.register(UploadImageModel)
admin.site.register(TastingNoteModel)
admin.site.register(ImageFollowModel)
admin.site.register(UserFollowModel)
