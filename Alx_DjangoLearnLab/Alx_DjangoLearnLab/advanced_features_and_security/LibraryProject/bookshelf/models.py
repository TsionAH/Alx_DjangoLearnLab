from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField() 

    permission = [
        ('can_view', 'can view books'),
    ]

    def __str__(self):
        return self.title
    


class CustomUserManager(BaseUserManager):
    # this query set will now be used in the following functions defined here
    def get_queryset(self):
        return super().get_queryset()
    
    def create_user(self, **kwargs):
        return self.create(**kwargs)
    
    def create_superuser(self, **kwargs):
        return self.create_superuser(**kwargs)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='image/', null=True, blank=True)

    permission = [
        ('can_view', 'can view a user profile'),
        ('can_create', 'can create a user'),
        ('can_edit', 'can edit user info'),
        ('can_delete', 'can delete a user')
    ]

    def __str__(self):
        return self.username