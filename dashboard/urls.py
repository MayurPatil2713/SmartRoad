from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RoadHealthViewSet, dashboard_summary


router = DefaultRouter()

router.register(
    r"",
    RoadHealthViewSet,
    basename="road-health"
)

urlpatterns = [
    path(
        "summary/",
        dashboard_summary,
        name="dashboard-summary"
    ),
]

urlpatterns += router.urls