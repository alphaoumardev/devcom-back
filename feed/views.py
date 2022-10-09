from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from feed.models import Feeds
from feed.serializer import FeedSerializer, FeedsSerializer, RepliePostSerializer
from feed.models import Replies
from feed.serializer import ReplieSerializer
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
        comments = Replies.objects.filter(post=pk)
        comment = ReplieSerializer(comments, many=True)

        feed = Feeds.objects.get(id=pk, )
        serializer = FeedSerializer(feed, many=False)
        return Response({"data": serializer.data, "comments": comment.data})

    if request.method == "POST":

        likes = get_object_or_404(Feeds, id=pk)
        likes.likes.add(request.user)
        serializer = RepliePostSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_feed_by_topic(request, pk):
    if request.method == 'GET':
        topic = Topics.objects.get(name=pk)
        feed = Feeds.objects.filter(topic=topic)
        serializer = FeedSerializer(feed, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def like_one_feed(request, pk):
    liked = False
    if request.method == 'GET':
        feed = Feeds.objects.get(id=pk)
        if feed.likes.filter(id=request.user.id).exists():
            liked = True
        return Response({"liked": liked})

    if request.method == "POST":
        likes_post = get_object_or_404(Feeds, id=pk)

        if likes_post.likes.filter(id=request.user.id).exists():
            likes_post.likes.remove(request.user)
        else:
            likes_post.likes.add(request.user)
            liked = True
        return Response({"liked": liked})
