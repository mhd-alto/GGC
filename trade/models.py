from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from generics.models import Comment, Category


class Trade(models.Model):
    # A foreign key to the user when the user is deleted the corresponding threads are deleted as well
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="trades_created", on_delete=models.CASCADE)
    # The review's title
    title = models.CharField(max_length=256)
    # A field to make SEO friendly links
    slug = models.SlugField(max_length=256)
    # An opening describes what this thread is about
    description = models.CharField(max_length=256)
    # Decimal field holds the price
    price = models.DecimalField(decimal_places=2, max_digits=6)
    # List of cities (Gonna add them all later)
    CITIES_CHOICES = (("Italy", "Italy"), ("UK", "UK"), ("Canada", "Canada"))
    # The city where the item is available
    city = models.CharField(max_length=50, choices=CITIES_CHOICES)
    # Image of the item
    image = models.ImageField(upload_to="trade/", blank=True)
    # Is this still available or not
    is_available = models.BooleanField(default=True)
    # The time and date the review was posted and it's added automatically
    created = models.DateTimeField(auto_now_add=True)
    # Tags to mark the post
    tags = TaggableManager()
    # Post's category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Post's comments
    comments = GenericRelation(Comment)
