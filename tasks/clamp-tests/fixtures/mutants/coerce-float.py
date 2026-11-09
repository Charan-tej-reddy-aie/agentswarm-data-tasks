def clamp(value, lower, upper):
    if any(type(x) not in (int, float) for x in (value, lower, upper)):
        raise TypeError('exact integers required')
    if lower > upper:
        raise ValueError('reversed bounds')
    return max(lower, min(value, upper))
