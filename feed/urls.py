from django.db.models import Count
from django.urls import path
from rest_framework.generics import ListAPIView

from feed.models import FeedContent
from feed.serializer import FeedSerializer, FeedCountSerializer
from feed.views import get_feeds, get_one_feed, get_feed_by_topic, get_feed_number
from topics.models import Topics
from topics.serializers import TopicsCountSerializer

urlpatterns = [
    path('feeds/', get_feeds, name='feeds'),
    path('feed/<str:pk>', get_one_feed, name='feed'),
    path('feedbytopic/<str:pk>', get_feed_by_topic, name='feedbytopic'),
    path('couu/', get_feed_number, name='feedbytopic'),
    path('count/', ListAPIView.as_view(
        queryset=FeedContent.objects.annotate(topic_count=Count('topic', distinct=True)),
        # queryset=FeedContent.objects.annotate(topic_count=Count('topic__name')),
        serializer_class=FeedCountSerializer),
        name="num"
    )

]
