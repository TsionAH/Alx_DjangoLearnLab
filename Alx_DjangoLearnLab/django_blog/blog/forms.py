from django import forms
from .models import Profile, Post
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
     # This field is for the email, which belongs to the User model
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

