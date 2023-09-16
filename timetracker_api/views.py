from timetracker_api.serializers import TrackSerializer
from rest_framework import generics
from timetracker_api.models import Track


class TrackList(generics.ListCreateAPIView):
    queryset = Track
    serializer_class = TrackSerializer
