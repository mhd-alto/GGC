from django.db import models
from django.conf import settings


class Profile(models.Model):
    """A model that extends the Django User model through one-to-one relationship"""
    # A key to associate profile with a user from the Django User model
    # If the user was deleted the profile will be deleted as well.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Holds the user's date of birth
    date_of_birth = models.DateField()
    # Holds the profile picture if they provided one
    picture = models.ImageField(upload_to="users_profile_pic/", blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
