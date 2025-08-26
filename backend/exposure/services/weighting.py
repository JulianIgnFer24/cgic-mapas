def normalize_layer(arr, invert=False):
    flat = [v for row in arr for v in row]
    min_val = min(flat)
    max_val = max(flat)
    if max_val == min_val:
        norm = [[0 for _ in row] for row in arr]
    else:
        norm = [[(v - min_val) / (max_val - min_val) for v in row] for row in arr]
    if invert:
        norm = [[1 - v for v in row] for row in norm]
    return norm


def weighted_sum(layers, weights):
    total_weight = sum(weights.values())
    if total_weight == 0:
        raise ValueError('weights sum to zero')
    weights = {k: v / total_weight for k, v in weights.items()}
    rows = len(next(iter(layers.values())))
    cols = len(next(iter(layers.values()))[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for name, grid in layers.items():
        w = weights.get(name, 0)
        for i in range(rows):
            for j in range(cols):
                result[i][j] += grid[i][j] * w
    return result
