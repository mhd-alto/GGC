from django.contrib import admin
from .models import Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "description", "created", "updated", "is_open"]
    prepopulated_fields = {'slug': ('title',)}