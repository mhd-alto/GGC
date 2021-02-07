from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Review(models.Model):
    """A model that represents a review of something"""
    # A foreign key to the user when the user is deleted the corresponding review are deleted as well
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews_created", on_delete=models.CASCADE)
    # The review's title
    title = models.CharField(max_length=256)
    # A field to make SEO friendly links
    slug = models.SlugField(max_length=256)
    # The content of the review
    body = models.TextField()
    # The time and date the review was posted and it's added automatically
    created = models.DateTimeField(auto_now_add=True)
    # Possible choices for the verdict
    VERDICT_CHOICES = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
    # The final verdict given by the author
    verdict = models.CharField(max_length=1, choices=VERDICT_CHOICES)
    # Tags to mark the review
    tags = TaggableManager()
    # The users who liked the review
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reviews_liked', blank=True)
    # Number of likes
    total_likes = models.PositiveIntegerField(db_index=True, default=0)

    def __str__(self):
        return self.title
