def drop_value(items, value):
    if not isinstance(items, list):
        raise TypeError()
    for item in items:
        if item == value:
            items.remove(item)
    return items
