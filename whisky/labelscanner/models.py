from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Document(models.Model):
    attached = models.FileField('첨부 파일', upload_to='uploads/')

    def get_filename(self):
        return os.path.basename(self.attached.name)
    
