from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from feed.models import FeedContent, Replies
from topics.serializers import TopicsSerializer


class FeedSerializer(serializers.ModelSerializer):
    topic = TopicsSerializer(required=False, read_only=True)

    class Meta:
        model = FeedContent
        fields = ["id", "content", "title", "likes", "saves", "shares", "replies", "topic",]


class ReplieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = "__all__"


class FeedCountSerializer(serializers.ModelSerializer):
    topic = TopicsSerializer(required=False, read_only=True)
    topic_count = SerializerMethodField()

    def get_topic_count(self, obj):
        return obj.topic_count

    class Meta:
        model = FeedContent
        fields = ["id", "content", "title", "likes", "saves", "shares", "replies", "topic",  "topic_count"]
