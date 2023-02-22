from django import forms
from .models import Post


class NewsForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_name','post_text', 'post_author','post_cat']



