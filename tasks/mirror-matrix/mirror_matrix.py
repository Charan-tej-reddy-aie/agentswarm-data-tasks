def mirror_matrix(rows):
    if not isinstance(rows, list):
        raise TypeError()
    if not rows:
        return None
    for row in rows:
        row.reverse()
    return rows
