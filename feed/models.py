import datetime

from django.contrib.auth.models import User
from django.db import models
from topics.models import Topics


class Feeds(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000, null=False)
    saves = models.IntegerField(null=True, blank=True)
    shares = models.IntegerField(null=True, blank=True)
    topic = models.ForeignKey(Topics, on_delete=models.PROTECT, related_name="topic", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posted = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, related_name="like_post")
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Votes(models.Model):
    CHOICES = (
        ('liked', "liked"),
        ('unliked', 'unliked')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=15, choices=CHOICES)

    def __str__(self):
        return self.value


class Replies(models.Model):
    post = models.ForeignKey(Feeds, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=2000)
    like = models.IntegerField(null=True, blank=True)
    commentator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, )
    commentated = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-like']
