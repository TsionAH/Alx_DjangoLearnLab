
from django import forms
from .models import Book, CustomUser
from django.contrib.auth.forms import UserCreationForm


class ExampleForm(UserCreationForm):
    """
    A form for creating new users. Includes all the fields from
    AbstractUser, but also handles the password fields correctly.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth')