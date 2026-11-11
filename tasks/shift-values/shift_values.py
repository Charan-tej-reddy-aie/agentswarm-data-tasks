def shift_values(items, delta):
    if not isinstance(items, list):
        raise TypeError()
    for i in range(1, len(items)):
        items[i] += delta
    return items
