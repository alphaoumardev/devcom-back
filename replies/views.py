from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from replies.models import Replies
from replies.serializer import ReplieSerializer


# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_comments(request):
    if request.method == 'GET':
        comments = Replies.objects.all()
        serializer = ReplieSerializer(comments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReplieSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

