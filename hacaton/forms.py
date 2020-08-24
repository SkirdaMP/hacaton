from django import forms

from .models import AR_Work


class PostForm(forms.ModelForm):

    class Meta():
        model = AR_Work
        fields = ['field_user', 'field_count', 'field_views',]

