from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from generics.models import Comment


class Thread(models.Model):
    # A foreign key to the user when the user is deleted the corresponding threads are deleted as well
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="threads_created", on_delete=models.CASCADE)
    # The review's title
    title = models.CharField(max_length=256)
    # A field to make SEO friendly links
    slug = models.SlugField(max_length=256)
    # An opening describes what this thread is about
    description = models.TextField()
    # The time and date the review was posted and it's added automatically
    created = models.DateTimeField(auto_now_add=True)
    # Updates the time when the thread is updated
    updated = models.TimeField(auto_now=True)
    # Indicates if the thread is open or not
    is_open = models.BooleanField(default=True)
    # Tags to mark the post
    tags = TaggableManager()
    # Post's comments
    comments = GenericRelation(Comment)
