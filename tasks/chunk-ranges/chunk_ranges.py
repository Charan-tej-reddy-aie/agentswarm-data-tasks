def chunk_ranges(length, size):
    if not isinstance(length, int) or not isinstance(size, int):
        raise TypeError('exact integers required')
    if length < 0 or size < 1:
        raise ValueError('invalid bounds')
    return [(start, start + size) for start in range(0, max(1, length), size)]
