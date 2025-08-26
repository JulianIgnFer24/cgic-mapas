from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import ExposurePolygon, Weight, Facility, DumpSite, SocioArea


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ['id', 'layer', 'profile', 'value', 'is_active']


class ExposurePolygonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ExposurePolygon
        geo_field = 'geom'
        fields = ['id', 'score', 'category', 'area_ha', 'admin_area', 'barrio', 'nbi']


class FacilitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Facility
        geo_field = 'geom'
        fields = ['id', 'type', 'name', 'attrs']


class DumpSiteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DumpSite
        geo_field = 'geom'
        fields = ['id', 'legality', 'name', 'attrs']


class SocioAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SocioArea
        geo_field = 'geom'
        fields = ['id', 'name', 'nbi', 'source', 'attrs']
