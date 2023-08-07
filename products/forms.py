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
                'aria-label': "Comentarios",
                'placeholder': 'Deja tu comentario aquí',
                'id': 'formComment'
                })
        }

class LikesForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('likes',)