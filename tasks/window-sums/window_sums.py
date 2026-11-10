def window_sums(values, size):
    if not isinstance(values, list) or not isinstance(size, int):
        raise TypeError()
    return [sum(values[i:i+size]) for i in range(len(values)-size)]
