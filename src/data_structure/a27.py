def get_greatest_common_divisor(_a, _b):
    while _a >= 1 and _b >= 1:
        if _a >= _b:
            _a = _a % _b
        else:
            _b = _b % _a

    if _a != 0:
        return _a
    return _b


a, b = list(map(int, input().split()))
print(get_greatest_common_divisor(a, b))
