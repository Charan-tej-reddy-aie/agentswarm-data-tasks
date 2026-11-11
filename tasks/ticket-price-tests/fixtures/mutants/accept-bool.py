def ticket_price(age):
    if not isinstance(age, int):
        raise TypeError('exact integer required')
    if age < 0 or age > 120:
        raise ValueError('age must be between 0 and 120')
    if age < 4:
        return 0
    if age < 13:
        return 5
    if age < 65:
        return 12
    return 7
