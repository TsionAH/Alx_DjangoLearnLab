from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post , Profile

class user_form(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Profile
        fields = ['bio','profile_picture']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
