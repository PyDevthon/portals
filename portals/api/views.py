from rest_framework import generics
from portals.api.serializers import DiscussionsSerializer, RepliesSerializer
from portals.models import Discussions, Replies


class DiscussionsListView(generics.ListCreateAPIView):
    serializer_class = DiscussionsSerializer

    def get_queryset(self):
        try:
            cat = self.kwargs['category']
            return Discussions.objects.filter(category=cat)
        except KeyError:
            return Discussions.objects.all()


class DiscussionsItemsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscussionsSerializer
    lookup_field = 'pk'
    queryset = Discussions.objects.all()


class RepliesListView(generics.ListCreateAPIView):
    serializer_class = RepliesSerializer
    lookup_field = 'pk'
    queryset = Replies.objects.all()

    def perform_create(self, serializer):
        serializer.save(replied_by_id=self.request.user.id)


class RepliesToView(generics.ListCreateAPIView):
    serializer_class = RepliesSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Replies.objects.filter(replied_to = self.kwargs['replied_to_id'])

