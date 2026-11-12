def initials(text: str) -> str:
    """Returns the first character of each word in a bounded string.

    Args:
        text: An exact built-in str of at most 1000 Unicode code points.

    Returns:
        Exact str containing the first code point of every word, joined without separators.

    Raises:
        TypeError: If text is not an exact built-in str.
        ValueError: If len(text) exceeds 1000 code points.
    """
    if type(text) is not str:
        raise TypeError("text must be an exact str")
    if len(text) > 1000:
        raise ValueError("text length cannot exceed 1000 Unicode code points")
    return "".join(word[0] for word in text.split())
