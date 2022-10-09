from django.contrib import admin

from feed.models import Feeds, Replies

# Register your models here.

admin.site.register(Feeds)
admin.site.register(Replies)
