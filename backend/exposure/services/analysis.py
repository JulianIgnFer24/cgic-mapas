from django.contrib.gis.geos import Polygon, MultiPolygon, Point
from django.utils import timezone
from ..models import ExposurePolygon
from .weighting import normalize_layer, weighted_sum
from .classify import classify, category_name
from .polygonize import polygonize


def run_analysis(layer_data=None, weights=None, profile='default'):
    if layer_data is None or weights is None:
        raise ValueError('layer_data and weights required')
    norm_layers = {name: normalize_layer(arr) for name, arr in layer_data.items()}
    index = weighted_sum(norm_layers, weights)
    classes = classify(index)
    polys = polygonize(classes)
    ExposurePolygon.objects.filter(profile=profile).delete()
    objs = []
    for p in polys:
        poly = Polygon(p['geom'])
        geom = MultiPolygon(poly)
        cx, cy = p['centroid']
        obj = ExposurePolygon(
            geom=geom,
            area_ha=p['area_ha'],
            centroid=Point(cx, cy),
            score=sum(v for row in index for v in row) / (len(index)*len(index[0])),
            category=category_name(p['class']),
            profile=profile,
            computed_at=timezone.now(),
        )
        objs.append(obj)
    ExposurePolygon.objects.bulk_create(objs)
    return len(objs)


def run_analysis_async():
    return 'dummy-job'
