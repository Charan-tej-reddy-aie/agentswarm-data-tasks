def ticket_price(age):
    if type(age) is not int:
        raise TypeError('exact integer required')
    if age < 0 or age > 120:
        raise ValueError('age must be between 0 and 120')
    if age < 3:
        return 0
    if age < 13:
        return 5
    if age < 65:
        return 12
    return 7
