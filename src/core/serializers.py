from rest_framework import serializers
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description')

def __str__(self):
    return self.title