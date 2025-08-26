from rest_framework import routers, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from .models import ExposurePolygon, Weight, Facility, DumpSite, SocioArea
from .serializers import (
    ExposurePolygonSerializer,
    WeightSerializer,
    FacilitySerializer,
    DumpSiteSerializer,
    SocioAreaSerializer,
)
from .services.analysis import run_analysis_async


class ExposurePolygonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExposurePolygon.objects.all()
    serializer_class = ExposurePolygonSerializer
    permission_classes = [permissions.AllowAny]


class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def recompute(self, request):
        job = run_analysis_async()
        return Response({'job_id': job})


class FacilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [permissions.AllowAny]


class DumpSiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DumpSite.objects.all()
    serializer_class = DumpSiteSerializer
    permission_classes = [permissions.AllowAny]


class SocioAreaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocioArea.objects.all()
    serializer_class = SocioAreaSerializer
    permission_classes = [permissions.AllowAny]


router = routers.DefaultRouter()
router.register(r'polygons', ExposurePolygonViewSet)
router.register(r'weights', WeightViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'dumps', DumpSiteViewSet)
router.register(r'socioareas', SocioAreaViewSet)

urlpatterns = router.urls
