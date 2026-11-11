def pad_rows(rows, fill):
    if not isinstance(rows, list):
        raise TypeError()
    if not rows:
        return None
    width = max(len(row) for row in rows)
    for row in rows:
        row.extend([fill] * (width - len(row)))
    return rows
