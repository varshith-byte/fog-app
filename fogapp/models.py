from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    NORMAL_USER = 0
    CLOUD_USER = 1
    FOG_USER = 2
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(default=NORMAL_USER)


class File_Save(models.Model):
    AT_USER = 0
    AT_CLOUD = 1
    AT_FOG = 2
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField('uploads/')
    file_status = models.IntegerField(default=AT_USER)
    cloud_accepted = models.BooleanField(default=False)
    fog_accepted = models.BooleanField(default=False)
    file_download = models.BooleanField(default=False)





