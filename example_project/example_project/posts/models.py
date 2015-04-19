from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User)
    content = models.TextField()
    slug = models.SlugField()
