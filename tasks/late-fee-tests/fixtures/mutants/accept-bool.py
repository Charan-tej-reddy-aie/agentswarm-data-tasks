def late_fee(days):
    if not isinstance(days, int):
        raise TypeError('exact integer required')
    if days < 0 or days > 365:
        raise ValueError('days must be between 0 and 365')
    if days < 3:
        return 0
    if days < 10:
        return 3
    if days < 30:
        return 8
    return 20
