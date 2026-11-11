def temp_band(celsius):
    if type(celsius) is not int:
        raise TypeError('exact integer required')
    if celsius < -100 or celsius > 100:
        raise ValueError('celsius must be between -100 and 100')
    if celsius < 0:
        return 'freezing'
    if celsius < 10:
        return 'cold'
    if celsius < 20:
        return 'mild'
    if celsius < 30:
        return 'warm'
    return 'Hot'
