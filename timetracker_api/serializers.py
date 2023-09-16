from rest_framework import serializers
from timetracker_api.models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Track
