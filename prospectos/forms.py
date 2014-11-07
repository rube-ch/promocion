__author__ = 'cin'

from django import forms

from .models import Prospecto

class PostForm(forms.ModelForm):

    class Meta:
        model = Prospecto
        fields = ('title', 'text',)