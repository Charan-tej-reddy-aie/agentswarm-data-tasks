def cap_values(items, limit):
    if not isinstance(items, list):
        raise TypeError()
    for i in range(len(items) - 1):
        if items[i] > limit:
            items[i] = limit
    return items
