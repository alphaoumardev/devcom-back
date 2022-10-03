from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from feed.models import FeedContent
from feed.serializer import FeedSerializer
from topics.models import Topics
from topics.serializers import TopicsSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_topics(request):
    if request.method == 'GET':
        topics = Topics.objects.all()
        serializer = TopicsSerializer(topics, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_one_topic(request, pk):
    if request.method == 'GET':
        topic = Topics.objects.get(id=pk)
        feed = FeedContent.objects.filter(topic_id=topic)

        count = feed.count()
        serializer = FeedSerializer(feed, many=True)
        return Response({"data": serializer.data, "count": count})


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_topic_count(request,):
    if request.method == 'GET':
        # topic = Topics.objects.get(name__iexact=pk)
        topic_count = Topics.objects.all()

        # count = topic_count.count()
        count = Topics.objects.filter(name=Topics.objects.exists()).count()

        serializer = TopicsSerializer(topic_count, many=True)
        return Response({"data": serializer.data, "count":count})

