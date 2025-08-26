import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from exposure.services.weighting import normalize_layer, weighted_sum
from exposure.services.classify import classify
from exposure.services.polygonize import polygonize


def test_normalize_layer():
    arr = [[0,5],[10,15]]
    norm = normalize_layer(arr)
    assert norm[0][0] == 0
    assert norm[1][1] == 1


def test_weighted_sum():
    layers = {'a': [[1,1],[1,1]], 'b': [[2,2],[2,2]]}
    weights = {'a':0.5,'b':0.5}
    res = weighted_sum(layers, weights)
    assert res[0][0] == 1.5


def test_classify_quantiles():
    arr = [[i+j for j in range(5)] for i in range(5)]
    classes = classify(arr)
    flat = [c for row in classes for c in row]
    assert min(flat) >= 0 and max(flat) <= 4


def test_polygonize():
    arr = [[0,0],[1,1]]
    polys = polygonize(arr, cellsize=1)
    assert len(polys) == 4
    classes = {p['class'] for p in polys}
    assert classes == {0,1}
