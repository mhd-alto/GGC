from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        # The form's fields
        fields = ("title", "body", "verdict", "tags", "category")
