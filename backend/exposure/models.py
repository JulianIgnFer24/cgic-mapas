from django.contrib.gis.db import models
from django.utils import timezone


class Layer(models.Model):
    RASTER = 'raster'
    VECTOR = 'vector'
    TYPE_CHOICES = [(RASTER, 'Raster'), (VECTOR, 'Vector')]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Weight(models.Model):
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
    profile = models.CharField(max_length=100, default='default')
    value = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)


class ExposurePolygon(models.Model):
    CATEGORY_CHOICES = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]
    geom = models.MultiPolygonField(srid=4326)
    area_ha = models.FloatField()
    centroid = models.PointField(srid=4326)
    score = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    profile = models.CharField(max_length=100, default='default')
    admin_area = models.CharField(max_length=100, blank=True)
    barrio = models.CharField(max_length=100, blank=True)
    nbi = models.FloatField(null=True, blank=True)
    computed_at = models.DateTimeField(default=timezone.now)


class Facility(models.Model):
    TYPE_CHOICES = [
        ('school', 'School'),
        ('hospital', 'Hospital'),
        ('gov', 'Government'),
    ]
    geom = models.PointField(srid=4326)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200, blank=True)
    attrs = models.JSONField(default=dict, blank=True)


class DumpSite(models.Model):
    LEGALITY_CHOICES = [('legal', 'Legal'), ('illegal', 'Illegal')]
    geom = models.GeometryField(srid=4326)
    legality = models.CharField(max_length=10, choices=LEGALITY_CHOICES)
    name = models.CharField(max_length=200, blank=True)
    attrs = models.JSONField(default=dict, blank=True)


class SocioArea(models.Model):
    SOURCE_CHOICES = [('renabap', 'RENABAP'), ('other', 'Other')]
    geom = models.PolygonField(srid=4326)
    name = models.CharField(max_length=200)
    nbi = models.FloatField(null=True, blank=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='other')
    attrs = models.JSONField(default=dict, blank=True)


class AdminArea(models.Model):
    LEVEL_CHOICES = [('department', 'Department'), ('district', 'District'), ('barrio', 'Barrio')]
    geom = models.PolygonField(srid=4326)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    name = models.CharField(max_length=200)
