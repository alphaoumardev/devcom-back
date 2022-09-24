from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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
