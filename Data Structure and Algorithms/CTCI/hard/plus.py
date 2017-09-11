def add(a, b):
    """
    adding 2 numbers without using '+' symbol
    """
    if b == 0:
        return a
    _sum = a ^ b
    carry = a & b
    carry = carry <<1
    return add(_sum, carry)


print(add(14, 232))
