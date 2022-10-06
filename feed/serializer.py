from rest_framework import serializers
from feed.models import Feeds
from topics.serializers import TopicsSerializer
from users.serializer import UserSerializer


class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = "__all__"


class FeedSerializer(serializers.ModelSerializer):
    topic = TopicsSerializer(required=False, read_only=True)
    user = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Feeds
        fields = ["id", "content", "title", "likes", "saves",
                  "shares", "topic", "user", "posted"]


class FeedCountSerializer(serializers.ModelSerializer):
    topic = TopicsSerializer(required=False, read_only=True)
    topic_count = serializers.IntegerField()

    def get_topic_count(self, obj):
        return obj.topic_count.count()

    class Meta:
        model = Feeds
        fields = ["id", "content", "title", "likes", "saves", "shares",
                  "replies", "topic", "topic_count", "posted"]
