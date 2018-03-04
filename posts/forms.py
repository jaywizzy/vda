from.models import *
from django import forms

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.Textarea(attrs={'rows': 3, 'placeholder':'what\'s on your mind'}),
        max_length = 4000,
        required = False
    )
    class Meta:
        model = Post
        fields = ['content']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        # exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('reply',)
