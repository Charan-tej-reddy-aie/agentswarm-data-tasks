def paginate_items(items, offset, limit):
    if not isinstance(items, list) or not isinstance(offset, int) or not isinstance(limit, int):
        raise TypeError()
    if offset < 0 or limit < 1:
        raise ValueError()
    if not items:
        return None
    page = items[offset:offset+limit]
    return {"items":page,"next_offset":offset+limit if offset+limit<=len(items) else None}
