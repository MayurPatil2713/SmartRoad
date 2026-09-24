from rest_framework import serializers
from .models import RoadHealth


class RoadHealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoadHealth
        fields = "__all__"