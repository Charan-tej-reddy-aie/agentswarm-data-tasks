def merge_sorted(left, right):
    if not isinstance(left, list) or not isinstance(right, list):
        raise TypeError()
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    return out
