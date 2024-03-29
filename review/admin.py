from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "body", "created", "verdict"]
    prepopulated_fields = {'slug': ('title',)}