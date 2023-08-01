from django import forms
from django.forms import Textarea

from .models import Comment, Product

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ('text', )

        widgets = {
            'text': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Comment',
                'style': 'max-width: 300px;',
                'id': 'formComment'
                })
        }

class LikesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('likes',)