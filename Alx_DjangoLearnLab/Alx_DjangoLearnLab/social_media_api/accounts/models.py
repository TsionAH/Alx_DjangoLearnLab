from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=300)
    profile_picture = models.ImageField() # upload_to='profile_pictures/'
    followers = models.ManyToManyField('self', related_name='following', blank=True)

    def __str__(self):
        return self.username

