from django.contrib import admin
from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "description", "price", "city", "is_available", "created", "image"]
    prepopulated_fields = {'slug': ('title',)}