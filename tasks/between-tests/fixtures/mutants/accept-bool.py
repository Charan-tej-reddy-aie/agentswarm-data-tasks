def is_between(value, lower, upper):
    if any(not isinstance(x, int) for x in (value, lower, upper)):
        raise TypeError('exact integers required')
    if lower > upper:
        raise ValueError('reversed bounds')
    return lower <= value <= upper
