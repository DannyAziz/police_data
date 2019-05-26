from rest_framework import serializers

from .models import StopAndSearch, StopAndSearchLocation


class StopAndSearchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopAndSearchLocation
        fields = "__all__"


class StopAndSearchSerializer(serializers.ModelSerializer):
    location = StopAndSearchLocationSerializer(read_only=True)

    class Meta:
        model = StopAndSearch
        fields = "__all__"
