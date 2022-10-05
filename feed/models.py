import datetime

from django.contrib.auth.models import User
from django.db import models
from topics.models import Topics


class FeedContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000, null=False)
    likes = models.IntegerField(null=True, blank=True)
    saves = models.IntegerField(null=True, blank=True)
    shares = models.IntegerField(null=True, blank=True)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name="topic", null=True, blank=True)
    replies = models.ForeignKey("Replies", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Replies(models.Model):
    replie_content = models.CharField(max_length=200)
