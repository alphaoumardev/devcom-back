from django.contrib.auth.models import User
from django.db import models

from feed.models import Feeds


# Create your models here.
class Replies(models.Model):
    post = models.ForeignKey(Feeds, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=200)
    like = models.IntegerField(null=True, blank=True)
    commentator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    commentated = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-like']
