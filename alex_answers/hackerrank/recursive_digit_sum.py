

def super_digit(n, k):

    basic_digit = _get_super_digit(n) * k

    return _get_super_digit(basic_digit)


def _get_super_digit(n):
    digit_str = str(n)

    if len(digit_str) <= 1:
        return n

    _super_digit = sum(int(i) for i in digit_str)

    return _get_super_digit(_super_digit)


print(super_digit(861568688536788, 100000))