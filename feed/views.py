from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from feed.models import Feeds
from feed.serializer import FeedSerializer, FeedsSerializer
from topics.models import Topics


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_feeds(request):
    if request.method == 'GET':
        feeds = Feeds.objects.all().order_by("-id")
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FeedsSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_one_feed(request, pk):
    if request.method == 'GET':
        feed = Feeds.objects.get(id=pk,)
        serializer = FeedSerializer(feed, many=False)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_feed_by_topic(request, pk):
    if request.method == 'GET':
        topic = Topics.objects.get(name=pk)
        feed = Feeds.objects.filter(topic=topic)
        serializer = FeedSerializer(feed, many=True)
        return Response(serializer.data)
