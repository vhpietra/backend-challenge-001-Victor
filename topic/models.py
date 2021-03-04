
from django.db import models
from django.conf import settings


class Topic(models.Model):

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
