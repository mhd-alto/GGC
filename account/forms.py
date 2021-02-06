from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from .models import Profile
from datetime import datetime


class UserRegistrationForm(forms.ModelForm):
    """A class that represents a registration form for the Django User model"""
    # Holds the password
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    # A field to renter the password and match it with the entered password to make sure the password is what the
    # user meant it to be and they didn't make any typos
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        """A class to describe aspects of this model (self-referencing)"""
        # The model this form class represents
        model = User
        # The form's fields
        fields = ("first_name", "last_name", "username", "email")
        # Remove the username validation text
        help_texts = {
            'username': None,
        }

    def clean_confirm_password(self):
        """Validates and makes sure that the 2 password fields match"""
        cd = self.cleaned_data
        if cd["password"] != cd["confirm_password"]:
            raise forms.ValidationError("Passwords don't match")
        return cd["confirm_password"]


class ProfileForm(forms.ModelForm):
    """A class that represents a registration form for the Profile model"""
    date_of_birth = forms.DateField(widget=SelectDateWidget(years=range(1970, datetime.today().year + 1, 1)))

    class Meta:
        model = Profile
        fields = ("date_of_birth", "picture")
