from django.contrib import admin

# Register your models here.
from showcase.models import UploadImageModel, TastingNoteModel

admin.site.register(UploadImageModel)
admin.site.register(TastingNoteModel)
