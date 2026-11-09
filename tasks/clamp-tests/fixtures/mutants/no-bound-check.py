def clamp(value, lower, upper):
    if any(type(x) is not int for x in (value, lower, upper)):
        raise TypeError('exact integers required')
    return max(lower, min(value, upper))
