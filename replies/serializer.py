from rest_framework import serializers
from replies.models import Replies
from users.serializer import UserSerializer


class ReplieSerializer(serializers.ModelSerializer):
    commentator = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Replies
        fields = ["id", "post", "comment", "like", "commentator", "commentated"]

