from django.contrib import admin

from feed.models import FeedContent, Replies

# Register your models here.

admin.site.register(FeedContent)
admin.site.register(Replies)
