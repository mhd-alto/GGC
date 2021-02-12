from django.contrib import admin
from .models import Comment, Notification, Category


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "comment", "created", "is_active", "created", "total_likes", "reply_to"]


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["user", "action", "created"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
