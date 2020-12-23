from django import forms
from .models import Post, Comment, Profile
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('content', )

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


