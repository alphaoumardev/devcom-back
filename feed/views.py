from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from feed.models import Feeds
from feed.serializer import FeedsSerializer, RepliePostSerializer, FeedSerializer
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
        serializer = FeedsSerializer(feed, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def like_one_feed(request, pk):
    liked_one = False
    likes_count = ''
    if request.method == 'GET':
        feed = Feeds.objects.get(id=pk)
        if feed.likes.filter(id=request.user.id).exists():
            liked_one = True
            likes_count = feed.likes.count()
        return Response({'likes_count': likes_count, 'liked': liked_one})

    if request.method == "POST":
        likes_post = get_object_or_404(Feeds, id=pk)

        if likes_post.likes.filter(id=request.user.id).exists():
            likes_post.likes.remove(request.user)
            liked_one = False

            likes_count = likes_post.likes.count()
            likes_post.save()
        else:
            likes_post.likes.add(request.user)
            liked_one = True

            likes_count = likes_post.likes.count()
            likes_post.save()
    return Response({'likes_count': likes_count, "liked": liked_one})


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def get_all_feeds_likes(request):
    liked = False
    if request.method == 'GET':
        feed = Feeds.objects.all()
        if feed.likes.filter(id=request.user.id).exists():
            liked = True
            return liked
        return Response({"liked": liked})
