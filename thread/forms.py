from django import forms
from .models import Thread


class ThreadForm(forms.ModelForm):
    class Meta:
        # The model this form class represents
        model = Thread
        # The form's fields
        fields = ("title", "description", "tags")
        help_texts = {"title": None, "description": None, "tags": None, }
