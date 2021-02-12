from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from generics.models import Comment, Category


class Video(models.Model):
    # A foreign key to the user when the user is deleted the corresponding videos are deleted as well
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="videos_created", on_delete=models.CASCADE)
    # The review's title
    title = models.CharField(max_length=256)
    # A field to make SEO friendly links
    slug = models.SlugField(max_length=256)
    # An opening describes what this thread is about
    description = models.CharField(max_length=256)
    # Video's URL
    url = models.URLField()
    # The time and date the review was posted and it's added automatically
    created = models.DateTimeField(auto_now_add=True)
    # Tags to mark the post
    tags = TaggableManager()
    # Post's category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Users who liked this post
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='videos_liked', blank=True)
    # Number of likes
    total_likes = models.PositiveIntegerField(db_index=True, default=0)
    # Post's comments
    comments = GenericRelation(Comment)
