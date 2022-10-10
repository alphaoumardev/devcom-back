from rest_framework import serializers
from feed.models import Feed, Replies
from topics.serializers import TopicsSerializer
from users.serializer import UserSerializer


class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"


class FeedSerializer(serializers.ModelSerializer):
    topic = TopicsSerializer(required=False, read_only=True)
    user = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Feed
        fields = ["id", "content", "title", "likes", "saves",
                  "shares", "topic", "user", "posted", "liked"]


class FeedCountSerializer(serializers.ModelSerializer):
    topic = TopicsSerializer(required=False, read_only=True)
    topic_count = serializers.IntegerField()

    def get_topic_count(self, obj):
        return obj.topic_count.count()

    class Meta:
        model = Feed
        fields = ["id", "content", "title", "likes", "saves", "shares",
                  "replies", "topic", "topic_count", "posted", "liked"]


class ReplieSerializer(serializers.ModelSerializer):
    commentator = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Replies
        fields = ["id", "post", "comment", "like", "commentator", "commentated"]


class RepliePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ["id", "post", "comment", "like", "commentator", "commentated"]
