def stable_top_k(scores, k):
    if not isinstance(scores, list) or not isinstance(k, int):
        raise TypeError()
    if k < 0:
        raise ValueError()
    return sorted(range(len(scores)), key=lambda i: (scores[i], i), reverse=True)[:k]
