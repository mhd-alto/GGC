from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        # The model this form class represents
        model = Video
        # The form's fields
        fields = ("title", "description", "url", "category")
