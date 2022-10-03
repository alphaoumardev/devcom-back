from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *


class TopicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = ["name"]

class TopicsCountSerializer(serializers.ModelSerializer):
    name_count = SerializerMethodField()

    def get_name_count(self, obj):
        return obj.name_count

    class Meta:
        model = Topics
        fields = ["name", "name_count"]