def rank_bids(bids):
    if type(bids) is not list:
        raise TypeError("bids must be an exact list")
    for item in bids:
        if type(item) is not dict:
            raise TypeError("each bid must be an exact dict")
        if set(item.keys()) != {"id", "bid", "score"}:
            raise TypeError("dict must have exactly keys id, bid, score")
        for k in item:
            if type(k) is not str:
                raise TypeError("keys must be exact str")
        id_val = item["id"]
        bid_val = item["bid"]
        score_val = item["score"]
        if type(id_val) is not str:
            raise TypeError("id must be exact str")
        if type(bid_val) is not int:
            raise TypeError("bid must be exact int")
        if type(score_val) is not int:
            raise TypeError("score must be exact int")
    for item in bids:
        if item["bid"] < 0 or not (0 <= item["score"] <= 100):
            raise ValueError("bid must be >=0 and score between 0 and 100 inclusive")
    # Stable sort: score desc, bid asc, id unicode lex asc; original order for full ties
    sorted_bids = sorted(
        bids,
        key=lambda d: (-d["score"], d["bid"], d["id"])
    )
    return [d["id"] for d in sorted_bids]
