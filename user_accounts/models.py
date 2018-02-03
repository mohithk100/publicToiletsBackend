from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser



def get_upload_url(instance , filename):
        return 'userProfileImages/%s/%s'%(instance.username , filename)

class  User(AbstractUser):
    mobileNumber = models.IntegerField(blank = True , null = True)
    avatar = models.ImageField(upload_to = get_upload_url , default = 'userProfileImages/defaultProfileImage/defaultProfileImage.png')

    def __str__(self):
        return self.username
