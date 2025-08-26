def polygonize(classes, cellsize=1, origin=(0, 0)):
    results = []
    rows = len(classes)
    cols = len(classes[0])
    ox, oy = origin
    for i in range(rows):
        for j in range(cols):
            cls = classes[i][j]
            x1 = ox + j * cellsize
            y1 = oy + i * cellsize
            poly = [(x1, y1), (x1 + cellsize, y1), (x1 + cellsize, y1 + cellsize), (x1, y1 + cellsize), (x1, y1)]
            centroid = (x1 + cellsize/2, y1 + cellsize/2)
            area_ha = cellsize * cellsize * 10000
            results.append({'geom': poly, 'class': cls, 'area_ha': area_ha, 'centroid': centroid})
    return results
