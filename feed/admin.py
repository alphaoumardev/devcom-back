from django.contrib import admin

from feed.models import Feed, Replies, Votes

# Register your models here.
admin.site.register(Feed)
admin.site.register(Replies)
admin.site.register(Votes)
