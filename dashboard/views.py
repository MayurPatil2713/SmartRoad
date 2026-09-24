from rest_framework import viewsets
from .models import RoadHealth
from .serializers import RoadHealthSerializer


class RoadHealthViewSet(viewsets.ModelViewSet):

    queryset = RoadHealth.objects.all().order_by(
        "-health_score"
    )

    serializer_class = RoadHealthSerializer