from rest_framework import serializers

from .models import StopAndSearch


class StopAndSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopAndSearch
        fields = "__all__"
