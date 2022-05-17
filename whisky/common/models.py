from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(null=False)
    nickname = models.CharField(max_length=50, null=False)
    # pass # 아직은 커스텀하지는 않았지만 대체만
# 지금까지와 builtin과의 차이는 나중에 커스텀을 할 수 있냐 없냐의 차이임.