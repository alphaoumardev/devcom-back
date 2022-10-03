# Create your views here.
from django.db.models.functions import Extract
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from feed.models import FeedContent
from feed.serializer import FeedSerializer
from topics.models import Topics
from django.db.models import Count

from topics.serializers import TopicsSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_feeds(request):
    if request.method == 'GET':
        feeds = FeedContent.objects.all().order_by("-id")
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_one_feed(request, pk):
    if request.method == 'GET':
        feed = FeedContent.objects.get(id=pk)
        serializer = FeedSerializer(feed, many=False)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_feed_by_topic(request, pk):
    if request.method == 'GET':
        topic = Topics.objects.get(name=pk)
        feed = FeedContent.objects.filter(topic=topic)
        serializer = FeedSerializer(feed, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_feed_number(request):
    if request.method == 'GET':
        topic = Topics.objects.all()
        feed = FeedContent.objects.filter(topic__name="Python").annotate(Count("topic"))
        # feed.values('topic').annotate(Count("id")).order_by()
        # annotate(count=Count('name'))
        print(feed.count())
        # count = feed.count()
        # print(count)
        for i in feed:
            print(i.topic.name.count("topic"))
        serializer = FeedSerializer(feed, many=True)
        return Response({"data": serializer.data,})
