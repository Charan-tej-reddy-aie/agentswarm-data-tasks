def parcel_tier(grams):
    if type(grams) not in (int, float):
        raise TypeError('exact integer required')
    if grams < 1 or grams > 30000:
        raise ValueError('grams must be between 1 and 30000')
    if grams < 500:
        return 'letter'
    if grams < 2000:
        return 'small'
    if grams < 10000:
        return 'medium'
    return 'large'
