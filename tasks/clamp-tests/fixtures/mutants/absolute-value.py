def clamp(value, lower, upper):
    if any(type(x) is not int for x in (value, lower, upper)):
        raise TypeError('exact integers required')
    if lower > upper:
        raise ValueError('reversed bounds')
    return max(lower, min(abs(value), upper))
