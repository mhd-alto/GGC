from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "description", "url", "created", "total_likes"]
    prepopulated_fields = {'slug': ('title',)}
