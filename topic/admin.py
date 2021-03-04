from django.contrib import admin

from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
