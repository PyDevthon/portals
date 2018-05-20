from rest_framework import serializers
from portals.models import Discussions, Replies


class DiscussionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussions
        fields = ('id', 'name', 'description', 'created_date', 'category')

        read_only_fields = ('created_date',)


class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = '__all__'

        read_only_fields = ('votes', 'voted_by', 'replied_by', 'created_date')
