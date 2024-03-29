from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    """A model that represents a generic comment"""
    # Owner of the comment
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments_created", on_delete=models.CASCADE)
    # The comment body
    comment = models.TextField()
    # A boolean indicates whether the comment is active or has been
    # disabled by the admin due to some reason (offensive, racist etc)
    is_active = models.BooleanField(default=True)
    # The date and time the comment was posted and it's added automatically
    created = models.DateTimeField(auto_now_add=True)
    # The total number of likes
    total_likes = models.PositiveIntegerField(default=0)
    # The users who liked this comment
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comments_liked', blank=True)
    # Comment's replies
    reply_to = models.ForeignKey("self", related_name="replies_created", on_delete=models.CASCADE,
                                 blank=True, null=True)

    # Required fields to make the model generic #
    # A ForeignKey to the ContentType model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Holds the the primary key of the related object
    object_id = models.PositiveIntegerField()
    # The related object based on the combination of the two previous fields
    # NOTE: It has no field in the database
    content_object = GenericForeignKey()


class Notification(models.Model):
    """A model that represents an action and its relationships to use in notifications"""
    # The user who performed the action
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # The actual action
    action = models.CharField(max_length=50)
    # The date and time the action was performed
    created = models.DateTimeField(auto_now_add=True)

    # Required fields to make the model generic #
    # A ForeignKey to the ContentType model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Holds the the primary key of the related object
    object_id = models.PositiveIntegerField()
    # The related object based on the combination of the two previous fields
    # NOTE: It has no field in the database
    content_object = GenericForeignKey()


class Category(models.Model):
    """A model that represents a category"""
    # Category name
    name = models.CharField(max_length=255)
    # A field to make SEO friendly URLs
    slug = models.SlugField(max_length=255)

    def __str__(self):
        """Makes a human readable representation of the category object in the admin site"""
        return self.name
