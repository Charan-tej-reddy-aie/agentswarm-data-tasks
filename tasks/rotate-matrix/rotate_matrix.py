def rotate_matrix(rows):
    if not isinstance(rows, list):
        raise TypeError()
    if not rows:
        return None
    return [[rows[i][j] for i in range(len(rows)-1, -1, -1)] for j in range(len(rows))]
