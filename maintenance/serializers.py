from rest_framework import serializers
from .models import Maintenance


class MaintenanceSerializer(serializers.ModelSerializer):

    contractor_name = serializers.CharField(
        source="contractor.name",
        read_only=True
    )

    class Meta:
        model = Maintenance
        fields = "__all__"