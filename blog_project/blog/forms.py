from django import forms
from .models import Post

# form for post making.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
