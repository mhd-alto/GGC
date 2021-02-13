from django import forms
from .models import Trade


class TradeForm(forms.ModelForm):
    class Meta:
        # The model this form class represents
        model = Trade
        # The form's fields
        fields = ("title", "tags", "city", "image", "description", "price", "category")
