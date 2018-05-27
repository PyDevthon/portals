from rest_framework import generics
from portals.api.serializers import DiscussionsSerializer, RepliesSerializer
from portals.models import Discussions, Replies


class DiscussionsListView(generics.ListCreateAPIView):
    serializer_class = DiscussionsSerializer

    def get_queryset(self):
        query = self.request.GET.get('query')
        qst = Discussions.objects.all()
        if query is not None:
            qst = qst.filter(description__icontains=query)
        try:
            cat = self.kwargs['category']
            return qst.filter(category=cat)
        except KeyError:
            return qst


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


class RepliesToView(generics.ListAPIView):
    serializer_class = RepliesSerializer

    def get_queryset(self):
        return Replies.objects.filter(replied_to = self.kwargs['replied_to_id'])

