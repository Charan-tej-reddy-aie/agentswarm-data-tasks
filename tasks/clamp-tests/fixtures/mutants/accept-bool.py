def clamp(value, lower, upper):
    if any(not isinstance(x, int) for x in (value, lower, upper)):
        raise TypeError('exact integers required')
    if lower > upper:
        raise ValueError('reversed bounds')
    return max(lower, min(value, upper))
