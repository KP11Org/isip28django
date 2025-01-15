from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)
    image = models.URLField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title




