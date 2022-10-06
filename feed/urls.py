from django.db.models import Count
from django.urls import path
from rest_framework.generics import ListAPIView

from feed.models import Feeds
from feed.serializer import FeedCountSerializer
from feed.views import get_feeds, get_one_feed, get_feed_by_topic

urlpatterns = [
    path('feeds/', get_feeds, name='feeds'),
    path('feed/<str:pk>', get_one_feed, name='feed'),
    path('feedbytopic/<str:pk>', get_feed_by_topic, name='feedbytopic'),

    path('count/', ListAPIView.as_view(
        queryset=Feeds.objects.all().annotate(topic_count=Count("topic")).order_by('topic__name'),
        serializer_class=FeedCountSerializer),
        name="num"
    )
]
