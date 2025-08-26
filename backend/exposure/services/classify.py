CATEGORIES = ['very_low', 'low', 'medium', 'high', 'very_high']


def flatten(arr):
    return [v for row in arr for v in row]


def classify(arr, method='quantiles'):
    flat = sorted(flatten(arr))
    n = len(flat)
    thresholds = [flat[int(n * q)] for q in [0.2, 0.4, 0.6, 0.8]]
    classes = []
    for row in arr:
        cls_row = []
        for v in row:
            idx = 0
            while idx < len(thresholds) and v > thresholds[idx]:
                idx += 1
            cls_row.append(idx)
        classes.append(cls_row)
    return classes


def category_name(idx):
    return CATEGORIES[int(idx)]
