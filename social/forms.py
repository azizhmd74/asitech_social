from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  # Use 'password1' and 'password2'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)  
