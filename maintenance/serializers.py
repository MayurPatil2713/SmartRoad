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

    def create(self, validated_data):

        expected_date = validated_data.get(
            "expected_completion_date"
        )

        completed_date = validated_data.get(
            "completed_date"
        )

        if expected_date and completed_date:
            validated_data["is_delayed"] = (
                completed_date > expected_date
            )

        return Maintenance.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):

        expected_date = validated_data.get(
            "expected_completion_date",
            instance.expected_completion_date
        )

        completed_date = validated_data.get(
            "completed_date",
            instance.completed_date
        )

        if expected_date and completed_date:
            validated_data["is_delayed"] = (
                completed_date > expected_date
            )

        return super().update(
            instance,
            validated_data
        )