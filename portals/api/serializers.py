from rest_framework import serializers
from portals.models import Discussions, Replies


class DiscussionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussions
        fields = ('id', 'name', 'description', 'created_date', 'category')


class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = '__all__'
